from django.urls import path

from applications.landing.apps import LandingConfig
from applications.landing.views import IndexView

app_name = LandingConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
