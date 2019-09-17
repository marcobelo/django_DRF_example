from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Heroes, Alliances
from .serializers import (
    HeroesSerializer,
    AlliancesSerializer,
    BuildRequestSerializer,
    BuildResponseSerializer,
)
from .views_functions import ListViewFactory


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
        return self.view.get(request)


class BuildView(APIView):
    def post(self, request):
        validated_request = BuildRequestSerializer(request.data)
        heroes = validated_request.data["heroes"]
        result = Heroes.build(heroes)
        validated_response = BuildResponseSerializer(result)

        # TODO: Remove alliances with no effects (effects: Null)
        return Response(validated_response.data)
