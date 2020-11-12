import http
import random
from typing import Any
from typing import Dict
from typing import Optional
from urllib.parse import parse_qs

from framework.consts import DIR_STATIC
from framework.consts import USER_COOKIE
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
    status = build_status(404)
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


def build_status(code: int) -> str:
    status = http.HTTPStatus(code)

    def _process_word(_word: str) -> str:
        if _word == "OK":
            return _word
        return _word.capitalize()

    reason = " ".join(_process_word(word) for word in status.name.split("_"))

    text = f"{code} {reason}"
    return text


def get_user_id(headers: Dict) -> Optional[str]:
    cookies = parse_qs(headers.get("COOKIE", ""))
    user_id = cookies.get(USER_COOKIE, [None])[0]

    return user_id


def get_request_headers(environ: dict) -> dict:
    environ_headers = filter(lambda _kv: _kv[0].startswith("HTTP_"), environ.items())
    request_headers = {key[5:]: value for key, value in environ_headers}
    return request_headers
