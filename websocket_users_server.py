import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for a in range(1, 6):
            await websocket.send(f"{a} Сообщение пользователя: {message}")

async def main():
    start_server = await websockets.serve(echo, "localhost", 8765)
    await start_server.wait_closed()



asyncio.run(main())