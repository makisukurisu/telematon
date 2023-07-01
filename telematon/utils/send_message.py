from __future__ import annotations

import asyncio
import typing

from .get_app import get_app

if typing.TYPE_CHECKING:
    from pyrogram import Client


async def make_call(app: Client, chat_id: int, message_text: str) -> None:
    async with app:
        await app.send_message(chat_id=chat_id, text=message_text)


def send_message(chat_id: int, message_text: str) -> None:
    try:
        even_loop = asyncio.get_event_loop()
    except RuntimeError:
        even_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(even_loop)

    app = get_app()

    return even_loop.run_until_complete(
        make_call(app, chat_id=chat_id, message_text=message_text)
    )
