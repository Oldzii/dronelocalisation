import socket
import asyncio
import struct
import time
import json
import websockets


class Object:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)


UDP_HOST = "127.0.0.1"
UDP_PORT = 7000
ADDRESS = (UDP_HOST, UDP_PORT)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(ADDRESS)


async def produce(message, host, port):
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()


unpack_data = struct.Struct('i i 5s 5s')
while True:
    data, addr = serverSocket.recvfrom(unpack_data.size)
    unpacked_data = unpack_data.unpack(data)
    print(unpacked_data)
    json_arr = unpacked_data
    data_to_send = Object()
    data_to_send.drone_id = json_arr[0]
    data_to_send.height = json_arr[1]
    data_to_send.latitude = (json_arr[2]).decode('utf-8')
    data_to_send.longitude = (json_arr[3]).decode('utf-8')
    data_to_send.time_send = time.time()
    json_string = json.dumps(data_to_send.to_json())
    print(data_to_send.to_json())
    print(json_string)
    asyncio.run(produce(message=json_string, host='127.0.0.1', port=4001))
