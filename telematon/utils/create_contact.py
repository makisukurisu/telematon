from __future__ import annotations

import asyncio
import typing

from pyrogram.types import InputPhoneContact

from .get_app import get_app

if typing.TYPE_CHECKING:
    from pyrogram import Client
    from pyrogram.raw.types.contacts.imported_contacts import ImportedContacts


async def make_call(app: Client, IPC: InputPhoneContact) -> ImportedContacts:
    async with app:
        return await app.import_contacts([IPC])


def create_contact(
    phone_number: str, first_name: str, last_name: str = ""
) -> ImportedContacts:
    try:
        even_loop = asyncio.get_event_loop()
    except RuntimeError:
        even_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(even_loop)

    app = get_app()

    return even_loop.run_until_complete(
        make_call(
            app,
            InputPhoneContact(
                phone=phone_number, first_name=first_name, last_name=last_name
            ),
        )
    )
