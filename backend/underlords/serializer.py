from rest_framework import serializers
from .models import Heroes, Alliances


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        depth = 1
        fields = ["tier", "name"]


class AlliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alliances
        depth = 1
        fields = ["name"]


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        depth = 1
        # fields = []
