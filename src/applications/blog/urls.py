from django.urls import include
from django.urls import path

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="main"),
    path("new/", views.NewPostView.as_view(), name="new_post"),
    path("reset/", views.WipeView.as_view(), name="reset_all"),
    path("post/<int:pk>/", views.PostView.as_view(), name="post"),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view(), name="post_delete"),
]
