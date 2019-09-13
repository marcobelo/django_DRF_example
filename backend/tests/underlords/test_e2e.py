import pytest
import requests
from django.core.management import call_command
from hamcrest import assert_that, has_entries, has_items

from tests.commons import BASE_URL

pytestmark = pytest.mark.django_db


def test_healthcheck(client):
    response = client.get(f"{BASE_URL}/healthcheck/", format="json")
    data = response.json()

    assert response.status_code == 200
    assert_that(data, has_entries({"message": "running..."}))


def test_list_heroes(client):
    call_command("loaddata", "underlords.json", verbosity=0)
    response = client.get(f"{BASE_URL}/heroes/", format="json")
    data = response.json()

    assert response.status_code == 200
    assert_that(list(data[0].keys()), has_items("tier", "name"))
