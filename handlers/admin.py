from telethon import events
from datetime import datetime
import os
import sys

from config import OWNER_ID, SUDO_USERS, CMD_HNDLR as hl


def register_admin_handlers(client):

    @client.on(events.NewMessage(pattern=f"\\{hl}ping"))
    async def ping(event):
        if event.sender_id in SUDO_USERS:
            start = datetime.now()

            msg = await event.reply("Pinging...")

            end = datetime.now()

            ms = (end - start).microseconds / 1000

            await msg.edit(f"Pong! `{ms} ms`")

    @client.on(events.NewMessage(pattern=f"\\{hl}reboot"))
    async def reboot(event):
        if event.sender_id == OWNER_ID:

            await event.reply("Restarting bot...")

            os.execl(sys.executable, sys.executable, *sys.argv)
