"""Run candidate Go code without access to trusted scoring assets."""

import os
from pathlib import Path
import signal
import subprocess


SCRATCH = Path('/tmp/lute-candidate')
UID = 65534


def protect(path: Path) -> None:
    for directory, dirs, files in os.walk(path, followlinks=False):
        for item in [Path(directory), *(Path(directory) / name for name in dirs + files)]:
            if item.is_symlink():
                continue
            os.chown(item, 0, 0)
            mode = item.stat().st_mode
            os.chmod(item, (mode & 0o755) | (0o555 if item.is_dir() else 0o444))


def prepare(repo: Path) -> None:
    if os.geteuid() != 0:
        raise RuntimeError('the trusted verifier must run as root')
    for parent in (Path('/logs'), Path('/workspace')):
        os.chown(parent, 0, 0)
        os.chmod(parent, 0o755)
    for path in (Path('/tests'), Path('/logs/verifier'), repo):
        protect(path)
    SCRATCH.mkdir(mode=0o700, exist_ok=True)
    os.chown(SCRATCH, UID, UID)


def cleanup() -> None:
    subprocess.run(['pkill', '-KILL', '-u', str(UID)], check=False,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_go(command, **kwargs):
    # No model credentials, user Go configuration, or writable trusted caches.
    kwargs.pop('env', None)
    env = {
        'PATH': '/opt/envpipe/runtime/bin:/usr/local/go/bin:/usr/bin:/bin',
        'HOME': str(SCRATCH), 'TMPDIR': str(SCRATCH),
        'GOCACHE': str(SCRATCH / 'go-cache'),
        'GOMODCACHE': '/opt/lute-go-mod', 'GOPATH': str(SCRATCH / 'go'),
        'GOPROXY': 'off', 'GOTOOLCHAIN': 'local', 'GOENV': 'off',
        'GIT_CONFIG_COUNT': '1', 'GIT_CONFIG_KEY_0': 'safe.directory',
        'GIT_CONFIG_VALUE_0': str(kwargs['cwd']),
    }
    command = ['setpriv', '--reuid=65534', '--regid=65534', '--clear-groups',
               '--no-new-privs', '--bounding-set=-all', *command]
    with subprocess.Popen(command, env=env, start_new_session=True,
                          **{k: v for k, v in kwargs.items() if k not in ('timeout', 'check')}) as process:
        try:
            stdout, stderr = process.communicate(timeout=kwargs.get('timeout'))
        except BaseException:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            raise
        finally:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)
