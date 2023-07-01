from __future__ import annotations

import asyncio
import typing

from .get_app import get_app

if typing.TYPE_CHECKING:
    from pyrogram import Client
    from pyrogram.types import User


async def make_call(app: Client, phone_number: str) -> User | None:
    async with app:
        all_contacts = await app.get_contacts()
        for contact in all_contacts:
            if contact.phone_number == phone_number:
                return contact
        else:
            return None


def get_contact(phone_number: str) -> User | None:
    phone_number = phone_number.replace("+", "").strip()
    try:
        even_loop = asyncio.get_event_loop()
    except RuntimeError:
        even_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(even_loop)

    app = get_app()

    return even_loop.run_until_complete(
        make_call(app, phone_number=phone_number)
    )
