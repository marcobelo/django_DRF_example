from rest_framework import serializers

# from .models import Heroes, Alliances


class HeroesSerializer(serializers.Serializer):
    tier = serializers.IntegerField()
    name = serializers.CharField()


class AlliancesSerializer(serializers.Serializer):
    name = serializers.CharField()


class HeroesPerTierSerializer(serializers.Serializer):
    tier_1 = serializers.ListField(serializers.CharField())
    tier_2 = serializers.ListField(serializers.CharField())
    tier_3 = serializers.ListField(serializers.CharField())
    tier_4 = serializers.ListField(serializers.CharField())
    tier_5 = serializers.ListField(serializers.CharField())


class EffectsPerAllianceInnerDict(serializers.Serializer):
    effect = serializers.CharField()
    quantity = serializers.IntegerField()


class EffectsPerAllianceSerializer(serializers.Serializer):

    # TODO: Find a way to make the alliances names not hardcoded
    assassin = EffectsPerAllianceInnerDict(required=False)
    blood_bound = EffectsPerAllianceInnerDict(required=False)
    brawny = EffectsPerAllianceInnerDict(required=False)
    deadeye = EffectsPerAllianceInnerDict(required=False)
    demon = EffectsPerAllianceInnerDict(required=False)
    demon_hunter = EffectsPerAllianceInnerDict(required=False)
    dragon = EffectsPerAllianceInnerDict(required=False)
    druid = EffectsPerAllianceInnerDict(required=False)
    elusive = EffectsPerAllianceInnerDict(required=False)
    heartless = EffectsPerAllianceInnerDict(required=False)
    human = EffectsPerAllianceInnerDict(required=False)
    hunter = EffectsPerAllianceInnerDict(required=False)
    inventor = EffectsPerAllianceInnerDict(required=False)
    knight = EffectsPerAllianceInnerDict(required=False)
    mage = EffectsPerAllianceInnerDict(required=False)
    primordial = EffectsPerAllianceInnerDict(required=False)
    savage = EffectsPerAllianceInnerDict(required=False)
    scaled = EffectsPerAllianceInnerDict(required=False)
    scrappy = EffectsPerAllianceInnerDict(required=False)
    shaman = EffectsPerAllianceInnerDict(required=False)
    troll = EffectsPerAllianceInnerDict(required=False)
    warlock = EffectsPerAllianceInnerDict(required=False)
    warrior = EffectsPerAllianceInnerDict(required=False)


class BuildRequestSerializer(serializers.Serializer):
    heroes = serializers.ListField(serializers.CharField())


class BuildResponseSerializer(serializers.Serializer):
    heroes_per_tier = HeroesPerTierSerializer()
    effects_per_alliance = EffectsPerAllianceSerializer()
