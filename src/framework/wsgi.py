from framework.utils import generate_404
from handlers.handle_image import handle_image
from handlers.handle_index import handle_index
from handlers.handle_style import handle_style

handlers = {"/xxx/": handle_style, "/image.jpg/": handle_image, "/": handle_index}


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handler = handlers.get(url, generate_404)

    status, headers, payload = handler(environ)

    start_response(status, list(headers.items()))

    yield payload
