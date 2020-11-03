import random

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
