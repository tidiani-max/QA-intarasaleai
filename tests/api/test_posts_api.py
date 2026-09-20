import allure
import pytest
import requests

TIMEOUT = 10


@allure.feature("API")
@pytest.mark.api
@pytest.mark.smoke
def test_get_post_contract(api_base_url):
    r = requests.get(f"{api_base_url}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    body = r.json()
    assert {"userId", "id", "title", "body"} <= body.keys()
    assert body["id"] == 1


@allure.feature("API")
@pytest.mark.api
@pytest.mark.regression
def test_create_post_echoes_payload(api_base_url):
    payload = {"title": "qa", "body": "automation", "userId": 7}
    r = requests.post(f"{api_base_url}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    assert r.json()["title"] == "qa"


@allure.feature("API")
@pytest.mark.api
@pytest.mark.regression
def test_unknown_resource_returns_404(api_base_url):
    r = requests.get(f"{api_base_url}/posts/999999", timeout=TIMEOUT)
    assert r.status_code == 404


@allure.feature("API")
@pytest.mark.api
@pytest.mark.regression
def test_response_time_budget(api_base_url):
    r = requests.get(f"{api_base_url}/posts", timeout=TIMEOUT)
    assert r.elapsed.total_seconds() < 2.0, "p-single latency budget exceeded"
