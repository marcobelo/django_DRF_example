from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Heroes
from .serializer import HeroesSerializer
from .views_functions import list_view


@api_view(["GET"])
def healthcheck(request):
    if request.method == "GET":
        return Response({"message": "running..."})


@api_view(["GET"])
def list_heroes(request):
    if request.method == "GET":
        return list_view(Heroes, HeroesSerializer)

