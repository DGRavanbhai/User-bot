import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH

def build_clients():
    clients = []

    for i in range(1, 11):
        session_string = os.getenv(f"SESSION_{i}", "").strip()
        if not session_string:
            continue

        client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
        clients.append(client)

    if not clients:
        raise RuntimeError("No SESSION_1 .. SESSION_10 values were found.")

    return clients
