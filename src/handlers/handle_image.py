from framework.utils import read_static


def handle_image(_environ):
    payload = read_static("image.jpg")
    status = "200 OK"
    headers = {"Content-type": "image/jpeg"}

    return status, headers, payload
