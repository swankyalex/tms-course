from datetime import timedelta
from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+
Visit http://{host}:{port}
..........................................
"""

_this_file_path = Path(__file__).resolve()

DIR_FRAMEWORK = _this_file_path.parent.resolve()

DIR_SRC = DIR_FRAMEWORK.parent.resolve()

DIR_REPO = DIR_SRC.parent.resolve()

DIR_STATIC = (DIR_SRC / "static").resolve()

DIR_STORAGE = (DIR_REPO / "db").resolve()

METHODS_WITH_REQUEST_BODY = {
    "POST",
}

USERS_STORAGE = (DIR_STORAGE / "users.json").resolve()

USER_COOKIE = "swanky"

USER_TTL = timedelta(minutes=5)

DATE_TIME_FMT = "%Y-%m-%d %H:%M:%S"
