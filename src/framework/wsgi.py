from urllib.parse import parse_qs

from framework.types import RequestT
from framework.utils import generate_404
from handlers.handle_error import make_error
from handlers.handle_hello import hello
from handlers.server_error import generate_500
from handlers.handle_image import handle_image
from handlers.handle_index import handle_index
from handlers.handle_style import handle_style

handlers = {"/xxx/": handle_style, "/image.jpg/": handle_image, "/": handle_index,
            "/e/": make_error, "/hello/": hello
            }


def application(environ: dict, start_response):
    try:
        path = environ["PATH_INFO"]

        handler = handlers.get(path, generate_404)

        request_headers = {
            key[5:]: environ[key]
            for key in filter(lambda i: i.startswith("HTTP_"), environ)
        }

        request = RequestT(
            method=environ["REQUEST_METHOD"],
            path=path,
            headers=request_headers,
            query=parse_qs(environ.get("QUERY_STRING") or "")
        )

        response = handler(request)

    except Exception:
        response = generate_500()

    start_response(response.status, list(response.headers.items()))

    yield response.payload
