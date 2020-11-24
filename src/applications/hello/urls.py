from django.urls import path

from applications.hello.views import hello
from applications.hello.views import hello_greet
from applications.hello.views import hello_reset

urlpatterns = [
    path("", hello),
    path("greet/", hello_greet),
    path("reset/", hello_reset),
]
