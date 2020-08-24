import requests


def test_open():
    r = requests.get("http://dockerlhost:8080/")

    assert r.status_code == 200, r.text
