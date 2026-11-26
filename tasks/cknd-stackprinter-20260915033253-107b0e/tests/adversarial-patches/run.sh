#!/usr/bin/env bash
# Replay exported patches using the task submitted alongside this package.
set -euo pipefail
export_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
exec python3 - "$export_dir" "$@" <<'PY_RUNNER'
import argparse
import collections
import datetime
import hashlib
import json
import math
import pathlib
import re
import signal
import shutil
import subprocess
import sys
import tarfile
import time
import uuid

ROOT = pathlib.Path(sys.argv[1]).resolve()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def checked_path(root, name):
    path = pathlib.PurePosixPath(name)
    require(name and not path.is_absolute() and ".." not in path.parts and "\\" not in name,
            "Invalid package/task path")
    target = root / name
    require(target.resolve().is_relative_to(root) and target.is_file() and not target.is_symlink(),
            "Missing or unsafe file: " + name)
    return target


def command(args, timeout=60, **kwargs):
    result = subprocess.run(args, timeout=timeout, **kwargs)
    if result.returncode:
        error = (result.stderr or result.stdout or b"")
        if isinstance(error, bytes):
            error = error.decode(errors="replace")
        raise RuntimeError("Command failed: " + " ".join(args[:3]) + ": " + error[-1200:])
    return result


def preflight(task, selected):
    manifest = load(ROOT / "manifest.json")
    runner = manifest.get("runner", {})
    require(runner.get("protocol") == "task-verifier/v1", "No supported runner configuration")
    require(digest(ROOT / "run.sh") == runner.get("sha256"), "run.sh hash mismatch")
    for name, sha in runner["task_files"].items():
        require(digest(checked_path(task, name)) == sha, "Submitted task differs: " + name)
    config = load(task / "tests/config.json")
    toml_id = re.search(r'^task_id\s*=\s*"([^"]+)"', (task / "task.toml").read_text(), re.M)
    require(manifest["task"]["id"] in {config.get("task_id"), toml_id and toml_id.group(1)} and
            config.get("base_commit") == manifest["task"]["base_commit"], "Task identity/base mismatch")
    require(config.get("reward_mode") == "VERIFIER_ONLY", "Runner supports deterministic VERIFIER_ONLY tasks")
    require(config.get("f2p") and config.get("p2p"), "Task selection sets missing")
    nodes = config["p2p"] + config["f2p"]
    require(all(isinstance(n, str) for n in nodes) and len(nodes) == len(set(nodes)), "Invalid node selection")
    patches = manifest["patches"]
    if selected:
        require(set(selected) <= {p["id"] for p in patches}, "Unknown --patch ID")
        patches = [p for p in patches if p["id"] in selected]
    require(patches, "No patches selected")
    for patch in patches:
        require(digest(checked_path(ROOT, patch["file"])) == patch["sha256"], "Patch hash mismatch")
        points = [p for p in manifest["verification_points"] if p["patch_id"] == patch["id"]]
        states = {p["application"] for p in points}
        require(points and len(states) == 1 and states <= {"clean_base", "reference_applied"},
                "Patch must have one supported start state")
        if "reference_applied" in states:
            ref = runner.get("reference_patch", {})
            require(ref.get("file") == "solution/solution.patch" and
                    runner["task_files"].get(ref["file"]) == ref.get("sha256"),
                    "Missing frozen reference dependency")
    return manifest, runner, config, patches


CONTAINER_COMMAND = r'''
set -euo pipefail
mkdir -p /logs
python3 - "$1" "$2" <<'PREFLIGHT'
import json, pathlib, subprocess, sys
repo="/workspace/repo"
head=subprocess.check_output(["git","-C",repo,"rev-parse","HEAD"],text=True).strip()
dirty=subprocess.check_output(["git","-C",repo,"status","--porcelain"],text=True).strip()
value={"base_commit":head,"pristine":not bool(dirty)}
pathlib.Path("/logs/replay-preflight.json").write_text(json.dumps(value))
if head != sys.argv[1] or dirty:
    raise SystemExit("Image repository must be pristine at the submitted task base commit")
if sys.argv[2] == "reference_applied":
    # Compose only inside the disposable container, preserving delivered bytes.
    value["application"] = "reference_applied"
    try:
        for patch in ("/logs/artifacts/reference.patch", "/logs/artifacts/delta.patch"):
            subprocess.run(["git", "-C", repo, "apply", "--index", "--binary", patch], check=True)
        attrs = pathlib.Path("/tmp/replay-attributes")
        attrs.write_text("* -diff\n")
        combined = subprocess.check_output(["git", "-C", repo, "-c", "core.attributesFile="+str(attrs),
                                            "diff", "--binary", "--full-index", head, "--"])
        pathlib.Path("/logs/artifacts/model.patch").write_bytes(combined)
    except subprocess.CalledProcessError:
        value["composition_failed"] = True
        pathlib.Path("/logs/replay-preflight.json").write_text(json.dumps(value))
        raise SystemExit("Reference/delta application failed before task evaluation")
    subprocess.run(["git", "-C", repo, "reset", "--hard", head], check=True)
    subprocess.run(["git", "-C", repo, "clean", "-fd"], check=True)
    value["composition_complete"] = True
    pathlib.Path("/logs/replay-preflight.json").write_text(json.dumps(value))
PREFLIGHT
cd /workspace/repo
bash /tests/test.sh
'''


def evaluate(folder, config, process_rc):
    if process_rc != 0:
        return {"formal_outcome": "EXECUTION_ERROR", "reason": "Task process did not complete normally"}
    logs = folder / "logs/verifier"
    details = load(logs / "reward-details.json")
    reward = load(logs / "reward.json").get("reward")
    hard_gate = load(logs / "hard-gate.json")
    gate = load(logs / "gate-reward.json")
    binary_report = (details.get("schema_version") == "deepswe-reward-details/v1"
                     and details.get("policy") == "deterministic_verifier_only"
                     and config.get("reward_mode") == "VERIFIER_ONLY")
    verifier_path = logs / "verifier-result.json"
    # This task's declared reports and test.sh do not emit verifier-result.json.
    # Its signed task files instead emit complete CTRF, gate and reward-details.
    if binary_report and not config.get("reports", {}).get("verifier") and not verifier_path.exists():
        verifier = {}
    else:
        verifier = load(verifier_path)
    if hard_gate.get("apply_failed") or gate.get("apply_failed"):
        return {"formal_outcome": "APPLY_FAILED", "reason": "Task reported candidate application failure"}
    if (hard_gate.get("infrastructure_error") or verifier.get("status") in {"INFRA_ERROR", "INCONCLUSIVE"}):
        return {"formal_outcome": "ENV_ERROR", "reason": details.get("termination_reason", "Invalid evaluation")}
    if gate.get("hard_gate_success") != 1 or hard_gate.get("success", hard_gate.get("passed")) is not True:
        return {"formal_outcome": "PRECONDITION_FAILED",
                "reason": details.get("termination_reason", "Hard gate blocked target evaluation")}
    valid = details.get("evaluation_valid") if binary_report else details.get("valid_for_statistics")
    if valid is not True:
        return {"formal_outcome": "ENV_ERROR", "reason": details.get("termination_reason", "Invalid evaluation")}
    ctrf = load(logs / "ctrf.json")["results"]["tests"]
    ids = [row.get("testId") or row.get("name") for row in ctrf]
    expected = config["p2p"] + config["f2p"]
    require(len(ids) == len(set(ids)) and set(ids) == set(expected), "Missing, duplicate or unexpected test nodes")
    states = {name: row.get("status") for name, row in zip(ids, ctrf)}
    require(all(s in {"passed", "failed"} for s in states.values()), "Nonterminal test results")
    require(type(reward) in (int, float) and math.isfinite(reward) and 0 <= reward <= 1, "Invalid reward")
    p2p_pass = sum(states[n] == "passed" for n in config["p2p"])
    f2p_pass = sum(states[n] == "passed" for n in config["f2p"])
    computed = f2p_pass / len(config["f2p"]) if p2p_pass == len(config["p2p"]) else 0
    if binary_report:
        eligible = p2p_pass == len(config["p2p"]) and f2p_pass == len(config["f2p"])
        require(gate.get("eligible_for_judge") is eligible, "Gate eligibility disagrees with test outcomes")
        computed = 1.0 if eligible else 0.0
    require(abs(reward - computed) < 0.00011, "Reward disagrees with task test-node outcomes")
    failed = [n for n in expected if states[n] == "failed"]
    return {"formal_outcome": "ACCEPTED" if not failed else "REJECTED", "reward": reward,
            "p2p_passed": p2p_pass, "p2p_total": len(config["p2p"]),
            "f2p_passed": f2p_pass, "f2p_total": len(config["f2p"]), "failed_nodes": failed,
            "reason": details.get("termination_reason", "")}


def run_patch(task, output, image, manifest, runner, config, patch, timeout):
    folder = output / patch["id"]
    folder.mkdir()
    container = "adversarial-export-" + uuid.uuid4().hex[:16]
    staged = folder / "inputs.tar"
    started = time.monotonic()
    result = {"patch_id": patch["id"], "patch_sha256": patch["sha256"]}
    created = False
    try:
        application = next(p["application"] for p in manifest["verification_points"]
                           if p["patch_id"] == patch["id"])
        # Copy only the already-submitted task assets; no host mount or jobs.
        with tarfile.open(staged, "w") as archive:
            for name in runner["task_files"]:
                if name.startswith("tests/"):
                    archive.add(checked_path(task, name), arcname=name, recursive=False)
            if application == "reference_applied":
                archive.add(checked_path(task, runner["reference_patch"]["file"]),
                            arcname="logs/artifacts/reference.patch", recursive=False)
            candidate_name = "delta.patch" if application == "reference_applied" else "model.patch"
            archive.add(checked_path(ROOT, patch["file"]), arcname="logs/artifacts/" + candidate_name, recursive=False)
        command(["docker", "create", "--name", container, "--network", "none", "--user", "0:0",
                 "--platform", runner["platform"],
                 "--cpus", str(runner["cpus"]), "--memory", str(runner["memory_mb"]) + "m",
                 "--entrypoint", "/bin/bash", image, "-c", CONTAINER_COMMAND,
                 "replay", manifest["task"]["base_commit"], application], capture_output=True)
        created = True
        with staged.open("rb") as source:
            command(["docker", "cp", "-", container + ":/"], stdin=source, capture_output=True)
        try:
            with (folder / "console.log").open("wb") as console:
                process = subprocess.run(["docker", "start", "-a", container], stdout=console,
                                         stderr=subprocess.STDOUT, timeout=timeout)
            rc = process.returncode
        except subprocess.TimeoutExpired:
            result.update(formal_outcome="TIMEOUT", reason="Task execution exceeded timeout")
            return result
        command(["docker", "cp", container + ":/logs", str(folder / "logs")], capture_output=True)
        baseline = load(folder / "logs/replay-preflight.json")
        require(baseline.get("base_commit") == manifest["task"]["base_commit"] and baseline.get("pristine"),
                "Image baseline/pristine check failed")
        if baseline.get("composition_failed"):
            result.update(formal_outcome="APPLY_FAILED", reason="Reference/delta composition failed")
            return result
        require(application != "reference_applied" or baseline.get("composition_complete"),
                "Reference/delta composition was not completed")
        result.update(evaluate(folder, config, rc))
        result["process_exit_code"] = rc
        return result
    except KeyboardInterrupt:
        result.update(formal_outcome="INTERRUPTED", reason="Run interrupted")
        return result
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.SubprocessError) as exc:
        result.update(formal_outcome="INCOMPLETE", reason=str(exc))
        return result
    finally:
        if created:
            try:
                cleanup = subprocess.run(["docker", "rm", "-f", container], capture_output=True, timeout=30)
                require(cleanup.returncode == 0, "Container cleanup failed")
                result["container_removed"] = True
            except (OSError, ValueError, subprocess.SubprocessError) as exc:
                result.update(formal_outcome="CLEANUP_FAILED", reason=str(exc), container_removed=False)
        staged.unlink(missing_ok=True)
        result["duration_seconds"] = round(time.monotonic() - started, 3)
        # The task verifier reports grading; it does not certify an independent oracle.
        result["verification_points"] = [
            {"id": p["id"], "expected_relation": p["expected_relation"],
             "formal_expectation_match":
                 (result.get("formal_outcome") == "REJECTED" if p["expected_relation"] == "reject" else
                  result.get("formal_outcome") == "ACCEPTED" if p["expected_relation"] in {"accept", "pass", "equivalent", "unchanged"} else None)
                 if result.get("formal_outcome") in {"ACCEPTED", "REJECTED"} else None,
             "target_assertion_confirmed": None}
            for p in manifest["verification_points"] if p["patch_id"] == patch["id"]]
        write(folder / "result.json", result)


def main():
    parser = argparse.ArgumentParser(prog="./run.sh", description="Use the submitted task's verifier to replay exported patches.")
    parser.add_argument("task_root", help="Task folder containing task.toml and tests/")
    parser.add_argument("--image", help="Reuse the task image; otherwise build/reuse tests/Dockerfile")
    parser.add_argument("--out", help="New results directory, outside this package and the task")
    parser.add_argument("--patch", action="append", help="Select a patch ID; default all")
    parser.add_argument("--timeout", type=int, help="Per-patch timeout in seconds")
    parser.add_argument("--check-only", action="store_true", help="Check task/patch hashes without executing tests")
    args = parser.parse_args(sys.argv[2:])
    task = pathlib.Path(args.task_root).resolve()
    manifest, runner, config, patches = preflight(task, args.patch)
    timeout = args.timeout if args.timeout is not None else runner["timeout_sec"]
    require(0 < timeout <= 86400, "Invalid timeout")
    if args.check_only:
        print(json.dumps({"valid": True, "patches": len(patches), "tests_executed": False}))
        return 0
    require(shutil.which("docker"), "Docker is required")
    command(["docker", "info"], capture_output=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = pathlib.Path(args.out).absolute() if args.out else ROOT.parent / (ROOT.name + "-results-" + stamp + "-" + uuid.uuid4().hex[:6])
    require(not output.exists(), "Results directory already exists")
    require(not output.resolve().is_relative_to(ROOT) and not output.resolve().is_relative_to(task),
            "Results must be outside the package and task")
    output.mkdir(parents=True)
    image = args.image
    if not image:
        key = hashlib.sha256(json.dumps(runner["task_files"], sort_keys=True).encode()).hexdigest()[:16]
        image = "adversarial-export/" + re.sub(r"[^a-z0-9_.-]", "-", manifest["task"]["id"].lower())[:80] + ":" + key
        inspected = subprocess.run(["docker", "image", "inspect", image], capture_output=True, timeout=30)
        if inspected.returncode:
            print("Building the submitted task's verifier image...", flush=True)
            with (output / "build.log").open("wb") as log:
                command(["docker", "build", "--platform", runner["platform"], "-t", image,
                         str(task / "tests")], timeout=runner["build_timeout_sec"], stdout=log, stderr=subprocess.STDOUT)
    image = command(["docker", "image", "inspect", "--format", "{{.Id}}", image],
                    capture_output=True).stdout.decode().strip()
    summary = {"task": manifest["task"], "image": image, "evaluation": "submitted_task_verifier",
               "target_assertions": "Not independently certified by this runner", "results": []}
    try:
        for patch in patches:
            print("Running " + patch["id"] + "...", flush=True)
            result = run_patch(task, output, image, manifest, runner, config, patch, timeout)
            summary["results"].append(result)
            write(output / "summary.json", summary)
            print(patch["id"] + ": " + result["formal_outcome"] + " reward=" + str(result.get("reward")), flush=True)
            if result["formal_outcome"] in {"INTERRUPTED", "CLEANUP_FAILED"}:
                break
    finally:
        write(output / "summary.json", summary)
    incomplete = any(r["formal_outcome"] not in {"ACCEPTED", "REJECTED"} for r in summary["results"])
    mismatch = any(p["formal_expectation_match"] is not True for r in summary["results"] for p in r["verification_points"])
    counts = dict(collections.Counter(r["formal_outcome"] for r in summary["results"]))
    print(json.dumps({"results": str(output), "counts": counts,
                      "expectation_mismatch": mismatch, "incomplete": incomplete}, ensure_ascii=False))
    return 130 if any(r["formal_outcome"] == "INTERRUPTED" for r in summary["results"]) else 2 if incomplete else 1 if mismatch else 0


if __name__ == "__main__":
    def terminate(signum, frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, terminate)
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted; active container cleanup attempted.", file=sys.stderr)
        raise SystemExit(130)
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.SubprocessError) as exc:
        print("Runner error: " + str(exc), file=sys.stderr)
        raise SystemExit(2)
PY_RUNNER
