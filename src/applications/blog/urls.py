from django.urls import include
from django.urls import path

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="main"),
    path("new/", views.NewPostView.as_view()),
    path("reset/", views.WipeView.as_view()),
    path("post/<int:pk>/", views.SinglePostView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", views.UpdatePostView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.DeletePostView.as_view()),
]
