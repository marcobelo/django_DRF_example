import pytest
import requests
from rest_framework.test import APIClient
from hamcrest import assert_that, has_entries

from tests.commons import BASE_URL

# pytestmark = pytest.mark.django_db
# from underlords.models import Country


def test_healthcheck():
    client = APIClient()
    response = client.get(f"{BASE_URL}/healthcheck/", format="json")
    data = response.json()

    assert response.status_code == 200
    assert_that(data, has_entries({"message": "running..."}))

