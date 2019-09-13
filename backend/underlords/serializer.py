from rest_framework import serializers
from .models import Heroes


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        depth = 1
        fields = ["tier", "name"]
