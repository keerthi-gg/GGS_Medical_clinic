import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope='session')
def clinic_server():
    with socket.socket() as listener:
        listener.bind(('127.0.0.1', 0))
        port = listener.getsockname()[1]

    base_url = f'http://127.0.0.1:{port}'
    process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', f'127.0.0.1:{port}', '--noreload'],
        cwd=REPOSITORY_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    deadline = time.monotonic() + 20
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError('Django development server exited before becoming ready.')
        try:
            with urlopen(base_url, timeout=1):
                break
        except (OSError, URLError):
            time.sleep(0.1)
    else:
        process.terminate()
        process.wait(timeout=5)
        raise TimeoutError('Django development server did not become ready.')

    yield base_url

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)