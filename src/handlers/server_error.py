import traceback

from framework.types import RequestT
from framework.types import ResponseT


def generate_500(_request: RequestT = None) -> ResponseT:
    document = traceback.format_exc()

    payload = document.encode()
    status = "500 Internal server error"
    headers_strings = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers_strings, payload)
