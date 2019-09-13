from django.urls import path
from underlords.views import healthcheck

urlpatterns = [path("healthcheck/", healthcheck, name="healthcheck")]

