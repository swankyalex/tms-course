from django.urls import path

from applications.hello.views import hello

urlpatterns = [
    path("", hello),
]
