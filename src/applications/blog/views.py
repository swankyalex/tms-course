from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from applications.blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(attrs={"rows": 2}),
        }


class AllPostsView(ListView):
    template_name = "blog/blog.html"
    model = Post

    def get_extended_context(self):
        context = {"form": PostForm()}

        return context


class NewPostView(CreateView):
    model = Post
    http_method_names = ["post"]
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:main")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class WipeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        Post.objects.all().delete()
        return reverse_lazy("blog:main")


class PostView(UpdateView):
    model = Post
    template_name = "blog/post.html"
    form_class = PostForm
    success_url = reverse_lazy("blog:main")

    def form_valid(self, form):
        self.object.edited = True
        return super().form_valid(form)


class DeletePostView(DeleteView):
    http_method_names = ["post"]
    model = Post
    success_url = reverse_lazy("blog:main")


class LikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        payload = {"ok": False, "nr_likes": 0, "reason": "unknown reason"}

        pk = self.kwargs.get("pk", 0)
        post = Post.objects.filter(pk=pk).first()

        if not post:
            payload.update({"reason": "post not found"})
        elif post.author == self.request.user:
            payload.update({"reason": "ne laikai svoi posty"})
        else:
            if post.is_liked_by(user):
                post.likers.remove(user)
            else:
                post.likers.add(user)
            post.save()

            post = Post.objects.get(pk=pk)
            payload.update({"ok": True, "nr_likes": post.nr_likes, "reason": None})

        return JsonResponse(payload)
