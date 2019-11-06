import pytest
import requests

def test_home():
    "GET request to url returns a 200"
    url = 'http://192.168.120.202/'
    resp = requests.get(url)
    assert resp.status_code == 200
