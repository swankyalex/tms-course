from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from framework.utils import read_static


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "index.html")

    return HttpResponse(result)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
]
