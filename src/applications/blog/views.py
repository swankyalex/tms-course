from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from applications.blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "object_list": Post.objects.all(),
    }
    result = render(request, "blog/blog.html", context=context)

    return HttpResponse(result)
