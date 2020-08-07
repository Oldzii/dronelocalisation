import asyncio
import logging
import websockets
import time

logging.basicConfig(level=logging.INFO)


async def consumer_handler(websocket):
    async for message in websocket:
        log_message((message, time.time()))


async def consume(hostname, port):
    websockets.websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websockets.websocket_resource_url) as websocket:
        await consumer_handler(websocket)


def log_message(message):
    logging.info(f"Message2: {message}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume(hostname="127.0.0.1", port=4001))
    loop.run_forever()
