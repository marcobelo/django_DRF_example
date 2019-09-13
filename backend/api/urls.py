from django.urls import path
from underlords.views import healthcheck, HeroesListView, AlliancesListView

urlpatterns = [
    path("healthcheck/", healthcheck, name="healthcheck"),
    path("heroes/", HeroesListView.as_view(), name="list_heroes"),
    path("alliances/", AlliancesListView.as_view(), name="list_alliances"),
]

