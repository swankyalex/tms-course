from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status
from framework.utils import read_static


def handle_style(_request: RequestT) -> ResponseT:
    payload = read_static("style.css")
    status = build_status(200)
    headers = {"Content-type": "text/css"}

    return ResponseT(status, headers, payload)
