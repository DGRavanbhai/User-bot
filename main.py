from __future__ import annotations

import asyncio

from clients import build_clients
from handlers.admin import register_admin_handlers


async def main() -> None:
    clients = build_clients()
    register_admin_handlers(clients)

    for client in clients:
        await client.start()

    print(f"Started {len(clients)} client(s).")
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))


if __name__ == "__main__":
    asyncio.run(main())
