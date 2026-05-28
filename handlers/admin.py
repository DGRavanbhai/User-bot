import os
import re
import sys
from datetime import datetime

from telethon import events
from config import OWNER_ID, SUDO_USERS, CMD_HNDLR as hl

def register_admin_handlers(client):
    prefix = re.escape(hl)

    @client.on(events.NewMessage(incoming=True, pattern=rf"^{prefix}ping(?:\s|$)(.*)"))
    async def ping(event):
        if event.sender_id not in SUDO_USERS:
            return

        start = datetime.now()
        msg = await event.reply("Pinging...")
        end = datetime.now()

        ms = (end - start).total_seconds() * 1000
        await msg.edit(f"Pong! `{ms:.2f} ms`")

    @client.on(events.NewMessage(incoming=True, pattern=rf"^{prefix}reboot(?:\s|$)(.*)"))
    async def reboot(event):
        if event.sender_id != OWNER_ID:
            return

        await event.reply("Restarting bot...")
        os.execl(sys.executable, sys.executable, *sys.argv)
