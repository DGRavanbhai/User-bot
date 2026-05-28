import asyncio

from clients import build_clients
from handlers.admin import register_admin_handlers

async def main():
    clients = build_clients()

    for client in clients:
        register_admin_handlers(client)

    for client in clients:
        await client.start()

    print(f"Started {len(clients)} client(s).")

    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

if __name__ == "__main__":
    asyncio.run(main())
