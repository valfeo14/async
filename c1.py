# WS client example

import asyncio
import websockets
from time import sleep
from random import randint
import numpy as np

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")
        arr = np.random.rand(5)
        barr = arr.tobytes()

        await websocket.send(barr)
        print("send  ", arr)

while(True) :
	asyncio.get_event_loop().run_until_complete(hello())
	sleep(randint(1, 5))
#asyncio.get_event_loop().run_until_complete(hello())