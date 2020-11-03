from framework.types import RequestT
from framework.types import ResponseT


def hello(request) -> ResponseT:

    name = request.query.get("name") or "anon"
    msg = f"Hello {name}"

    payload = msg.encode()
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)
