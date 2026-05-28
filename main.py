async def main():
    clients = build_clients()

    for client in clients:
        register_admin_handlers(client)

    for client in clients:
        await client.start()

    await asyncio.gather(*(client.run_until_disconnected() for client in clients))
