from framework import settings
from framework.consts import USER_COOKIE
from framework.consts import USER_TTL
from framework.db import save_user
from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def hello(request) -> ResponseT:
    handlers = {
        "GET": handle_hello_get,
        "POST": handle_hello_post,
    }

    handler = handlers.get(request.method)

    response = handler(request)
    return response


def handle_hello_get(request: RequestT) -> ResponseT:

    base_html = read_static("_base.html").decode()
    hello_html = read_static("hello.html").decode()

    result = hello_html.format(
        address_header=request.user.address or "грёз",
        address_value=request.user.address or "",
        name_header=request.user.name or "бродяга",
        name_value=request.user.name or "",
    )

    result = base_html.format(xxx=result)

    payload = result.encode()
    status = build_status(200)
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)


def handle_hello_post(request: RequestT) -> ResponseT:

    form_data = request.form_data

    name = form_data.get("name", [None])[0]
    address = form_data.get("address", [None])[0]

    request.user.name = name
    request.user.address = address

    save_user(request.user)

    status = build_status(302)
    headers = {
        "Location": "/h/",
        "Set-Cookie": (
            f"{USER_COOKIE}={request.user.id};"
            f" Domain={settings.HOST};"
            f" HttpOnly;"
            f" Max-Age={USER_TTL.total_seconds()}"
        ),
    }

    response = ResponseT(
        headers=headers,
        status=status,
    )

    return response
