import random
from typing import Any
from typing import Dict
from urllib.parse import parse_qs

from framework.consts import DIR_STATIC
from framework.types import RequestT
from framework.types import ResponseT


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def generate_404(request: RequestT) -> ResponseT:

    url = request.path
    pin = random.randint(1, 1000)
    msg = f"Hello world! Your path: {url} not found. Pin: {pin}"

    headers_strings = [f"{h} -> {v}" for h, v in request.headers.items()]

    headers_txt = ""
    for item in headers_strings:
        headers_txt = headers_txt + item + "\n"

    document = f"""404! path: {url}, pin{pin}

{headers_txt}
"""

    payload = document.encode()
    status = "404 Not Found"
    headers_strings = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers_strings, payload)


def get_form_data(body: bytes) -> Dict[str, Any]:
    qs = body.decode()
    form_data = parse_qs(qs or "")
    return form_data


def get_body(environ: dict) -> bytes:
    fp = environ["wsgi.input"]
    cl = int(environ.get("CONTENT_LENGTH") or 0)

    if not cl:
        return b""

    content = fp.read(cl)

    return content
