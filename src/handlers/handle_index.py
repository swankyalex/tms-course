from framework.utils import read_static


def handle_index(_environ):
    base_html = read_static("_base.html").decode()
    index_html = read_static("index.html").decode()

    result = base_html.format(xxx=index_html)
    result = result.encode()

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    return status, headers, result
