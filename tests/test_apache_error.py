import pytest
import requests

def test_home():
    "GET request to url returns a 200"
    url = 'http://192.168.120.202/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_index():
    "Index page states 'WEBSERVER RUNNING'"
    url = 'http://192.168.120.202/'
    resp = requests.get(url)
    body = resp.content
    assert body == "<H1>SERVER RUNNING</H1>"