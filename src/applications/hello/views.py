from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


def hello(request: HttpRequest) -> HttpResponse:
    name = request.session.get("name")
    address = request.session.get("address")

    context = {
        "name_header": name or "бродяга",
        "address_header": address or "localhost",
        "name_value": name or "",
        "address_value": address or "",
    }
    result = render(request, "hello/hello.html", context=context)

    return HttpResponse(result)


def hello_greet(request: HttpRequest) -> HttpResponse:
    name = request.POST.get("name")
    address = request.POST.get("address")
    request.session["name"] = name
    request.session["address"] = address
    return redirect("/h/")


def hello_reset(request: HttpRequest) -> HttpResponse:
    request.session.clear()
    return redirect("/h/")
