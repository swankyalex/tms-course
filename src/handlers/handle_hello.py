from framework.types import ResponseT
from framework.utils import read_static


def hello(request) -> ResponseT:
    name = (request.query.get("name") or [None])[0]
    address = (request.query.get("address") or [None])[0]

    base_html = read_static("_base.html").decode()
    hello_html = read_static("hello.html").decode()

    result = hello_html.format(
        address_header=address or "nowhere",
        address_value=address or "",
        name_header=name or "бродяга",
        name_value=name or "",
    )
    result = base_html.format(xxx=result)

    payload = result.encode()
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)
