from django.urls import path

from applications.blog.views import blog_reset
from applications.blog.views import index
from applications.blog.views import new_post_view

urlpatterns = [path("", index), path("new/", new_post_view), path("reset/", blog_reset)]
