import os

import requests


def test_open():
    host = os.environ.get("TESTS_WEB_HOST")
    if host is None:
        host = "localhost"

    r = requests.get(f"http://{host}:8080/")

    assert r.status_code == 200, r.text
