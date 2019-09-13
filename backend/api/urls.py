from django.urls import path
from underlords.views import healthcheck, list_heroes

urlpatterns = [
    path("healthcheck/", healthcheck, name="healthcheck"),
    path("heroes/", list_heroes, name="list_heroes"),
]

