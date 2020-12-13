from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
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
