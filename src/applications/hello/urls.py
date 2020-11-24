from django.urls import path

from applications.hello.views import hello, hello_greet, hello_reset

urlpatterns = [
    path("", hello),
    path("greet/", hello_greet),
    path("reset/", hello_reset),
]
