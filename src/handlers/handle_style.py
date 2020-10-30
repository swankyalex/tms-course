from framework.utils import read_static


def handle_style(_environ):
    payload = read_static("style.css")
    status = "200 OK"
    headers = {"Content-type": "text/css"}

    return status, headers, payload
