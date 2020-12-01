from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from applications.blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "object_list": Post.objects.all(),
    }
    result = render(request, "blog/blog.html", context=context)

    return HttpResponse(result)


def new_post_view(request):
    title = request.POST["title"]
    content = request.POST["content"]

    post = Post(
        title=title,
        content=content,
    )
    post.save()

    return redirect("/b")


def blog_reset(request: HttpRequest) -> HttpResponse:
    Post.objects.all().delete()
    return redirect("/b/")
