from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import RedirectView

from applications.blog.models import Post


class AllPostsView(ListView):
    template_name = "blog/blog.html"
    model = Post


class NewPostView(CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = "/b/"


class WipeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return "/b/"
