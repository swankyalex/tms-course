from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="main"),
    path("new/", views.NewPostView.as_view(), name="new_post"),
    path("reset/", views.WipeView.as_view(), name="reset_all"),
    path("post/<int:pk>/", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view(), name="post_delete"),
    path("post/<int:pk>/like/", csrf_exempt(views.LikeView.as_view()), name="like"),
]
