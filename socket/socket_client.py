import asyncio
import websockets


async def send_stream():
    count = 0
    server_stop = False
    async with websockets.connect("ws://localhost:8001") as websocket:
        while not server_stop:
            count += 1
            await websocket.send(f"Hello {count} world!")

asyncio.run(send_stream())