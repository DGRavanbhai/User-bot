from __future__ import annotations

from typing import List

from telethon import TelegramClient
from telethon.sessions import StringSession

from config import API_HASH, API_ID, SESSION_STRINGS


def build_clients() -> List[TelegramClient]:
    if not API_ID or not API_HASH:
        raise RuntimeError("Set API_ID and API_HASH in your environment or .env file.")

    clients: List[TelegramClient] = []
    for index, session_string in enumerate(SESSION_STRINGS, start=1):
        if not session_string:
            continue
        client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
        clients.append(client)

    if not clients:
        raise RuntimeError("No SESSION_1 .. SESSION_10 values were found.")

    return clients
