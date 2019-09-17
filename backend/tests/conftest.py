import pytest
from django.core.management import call_command


@pytest.fixture(scope="function", name="load_database_fixtures")
def fixture_load_database_fixtures():
    call_command("loaddata", "db_fixture.json", verbosity=0)
