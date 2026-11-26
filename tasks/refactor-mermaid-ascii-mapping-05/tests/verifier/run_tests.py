#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    args.report.parent.mkdir(parents=True, exist_ok=True)
    suites = ET.Element("testsuites")
    failed = False
    commands = (
        ("p2p", "tests/p2p/run_p2p.py", ["--selectors", config["p2p_select"]]),
        ("f2p", "tests/f2p/run_f2p.py", ["--config", str(args.config)]),
    )
    for role, script, arguments in commands:
        report = args.report.with_name(role + ".xml")
        report.unlink(missing_ok=True)
        process = subprocess.run([sys.executable, script, *arguments, "--report", str(report)])
        failed = failed or process.returncode != 0
        document = ET.parse(report).getroot()
        if document.tag == "testsuite":
            suites.append(document)
        elif document.tag == "testsuites":
            suites.extend(document)
        else:
            raise ValueError("unrecognized JUnit report root: " + role)
    ET.ElementTree(suites).write(args.report, encoding="utf-8", xml_declaration=True)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
