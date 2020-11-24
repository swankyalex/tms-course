from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    result = render(request, "landing/index.html")

    return HttpResponse(result)
