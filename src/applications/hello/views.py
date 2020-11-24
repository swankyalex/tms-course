from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello(request: HttpRequest) -> HttpResponse:
    result = render(request, "hello/hello.html")

    return HttpResponse(result)
