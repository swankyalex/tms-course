import traceback

from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import build_status


def generate_500(_request: RequestT = None) -> ResponseT:
    document = traceback.format_exc()

    payload = document.encode()
    status = build_status(500)
    headers_strings = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers_strings, payload)
