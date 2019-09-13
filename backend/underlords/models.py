from django.db import models


class Heroes(models.Model):
    tier = models.IntegerField(null=False)
    name = models.TextField(max_length=80, null=False, unique=True)
    brazilian_name = models.TextField(max_length=80, null=False, unique=True)


class Alliances(models.Model):
    name = models.TextField(max_length=80, null=False, unique=True)


class HeroesAlliances(models.Model):
    class Meta:
        unique_together = (("hero", "alliance"),)

    hero = models.ForeignKey(Heroes, on_delete=models.CASCADE)
    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE)


class AlliancesEffects(models.Model):
    class Meta:
        unique_together = (("alliance", "quantity"),)

    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    effect = models.TextField(null=False)
