import pytest
import requests
from hamcrest import assert_that, has_entries
from tests.commons import BASE_URL


def test_healthcheck():
    response = requests.get(f"{BASE_URL}/healthcheck/")
    data = response.json()

    assert response.status_code == 200
    assert_that(data, has_entries({"message": "running..."}))

