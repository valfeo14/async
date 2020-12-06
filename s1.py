# WS server example

import asyncio
import websockets
import numpy as np

arr = np.random.rand(5)

async def hello(websocket, path):
    barr = await websocket.recv()
    arr = np.frombuffer(barr)
    print("recieve = ", arr)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
#first comment
