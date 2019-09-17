import pytest
from hamcrest import assert_that, has_items

from underlords.serializers import HeroesSerializer, AlliancesSerializer


def test_heroes_serializer():
    data = {"tier": 2, "name": "abaddon"}
    result = HeroesSerializer(data=data)

    assert result.is_valid()
    assert_that(result.data.keys(), has_items("tier", "name"))


def test_alliance_serializer():
    data = {"name": "assassin"}
    result = AlliancesSerializer(data=data)

    assert result.is_valid()
    assert_that(result.data.keys(), has_items("name"))

