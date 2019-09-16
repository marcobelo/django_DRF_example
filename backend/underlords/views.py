from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Heroes, Alliances
from .serializer import HeroesSerializer, AlliancesSerializer
from .views_functions import ListViewFactory, list_view


@api_view(["GET"])
def healthcheck(request):
    if request.method == "GET":
        return Response({"message": "running..."})


class HeroesListView(APIView):
    view = ListViewFactory(HeroesSerializer, Heroes)

    def get(self, request):
        return self.view.get(request)


class AlliancesListView(APIView):
    view = ListViewFactory(AlliancesSerializer, Alliances)

    def get(self, request):
        heroes = [
            "medusa",
            "drow ranger",
            "tidehunter",
            "luna",
            "chaos knight",
            "omniknight",
            "dragon knight",
            "abbaddon",
            "batrider",
            "troll warlord",
        ]

        res = Heroes.build(heroes)
        import ipdb

        ipdb.set_trace()
        for hero in res:
            print(f"{hero.name} - {hero.tier}")
        return self.view.get(request)

