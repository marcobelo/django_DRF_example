import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="session", name="client")
def fixture_client():
    return APIClient()
