import os
from run import Bot
from utils import asyncio


async def handle_http_request(reader, writer):
    try:
        # Read the request headers (limit to 1024 bytes)
        await reader.read(1024)
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 12\r\n"
            "Connection: close\r\n"
            "\r\n"
            "Bot is alive"
        )
        writer.write(response.encode('utf-8'))
        await writer.drain()
    except Exception as e:
        print(f"Error handling HTTP request: {e}")
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def start_health_check_server():
    port = os.getenv('PORT')
    if not port:
        print("PORT environment variable not set. Skipping health check server (running locally).")
        return
    try:
        server = await asyncio.start_server(handle_http_request, '0.0.0.0', int(port))
        print(f"Health check server started on port {port}")
    except Exception as e:
        print(f"Failed to start health check server: {e}")


async def ping_self():
    ping_url = os.getenv('PING_URL') or os.getenv('WEB_URL')
    if not ping_url:
        return
    print(f"Self-ping task started for URL: {ping_url}")
    await asyncio.sleep(30)
    while True:
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(ping_url) as response:
                    print(f"Self-ping status: {response.status}")
        except Exception as e:
            print(f"Self-ping failed: {e}")
        await asyncio.sleep(600)  # Ping every 10 minutes


async def main():
    # Start health check server if PORT is set (useful for free cloud hosting like Render/Koyeb)
    await start_health_check_server()
    # Start self-pinging task if PING_URL or WEB_URL is configured
    asyncio.create_task(ping_self())

    await Bot.initialize()
    await Bot.run()


asyncio.run(main())
