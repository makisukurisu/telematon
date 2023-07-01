import pyrogram
from get_docker_secret import get_docker_secret
from pyrogram.enums import ParseMode


def get_app() -> pyrogram.Client:
    app = pyrogram.Client(
        name="telematon",
        api_id=get_docker_secret("app_api_id").strip(),
        api_hash=get_docker_secret("app_api_hash").strip(),
        session_string=get_docker_secret("session_string").strip(),
        parse_mode=ParseMode.HTML,
    )
    return app
