from django.db import models


class Alliances(models.Model):
    name = models.TextField(max_length=80, null=False, unique=True)


class AlliancesEffects(models.Model):
    class Meta:
        unique_together = (("alliance", "quantity"),)

    alliance = models.ForeignKey(Alliances, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    effect = models.TextField(null=False)


class Heroes(models.Model):
    tier = models.IntegerField(null=False)
    name = models.TextField(max_length=80, null=False, unique=True)
    brazilian_name = models.TextField(max_length=80, null=False, unique=True)
    alliances = models.ManyToManyField(Alliances)

    @classmethod
    def build(cls, heroes_list):
        heroes = cls.objects.filter(name__in=heroes_list)
        heroes_per_tier = {}
        effects_per_alliance = {}
        for hero in heroes:
            try:
                heroes_per_tier[f"tier_{hero.tier}"].append(hero.name)
            except KeyError:
                heroes_per_tier[f"tier_{hero.tier}"] = [hero.name]

            for alliance in hero.alliances.all():
                try:
                    effects_per_alliance[alliance.name]["quantity"] += 1
                except KeyError:
                    effects_per_alliance[alliance.name] = {}
                    effects_per_alliance[alliance.name]["quantity"] = 1
                    effects_per_alliance[alliance.name]["id"] = alliance.id

        for alliance in effects_per_alliance:
            alliance_temp = effects_per_alliance[alliance]
            effects = AlliancesEffects.objects.filter(
                alliance_id=alliance_temp["id"], quantity__lte=alliance_temp["quantity"]
            ).order_by("-quantity")
            try:
                effects_per_alliance[alliance]["effect"] = effects[0].effect
            except IndexError:
                effects_per_alliance[alliance]["effect"] = None

        return {
            "heroes_per_tier": heroes_per_tier,
            "effects_per_alliance": effects_per_alliance,
        }
