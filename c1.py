# WS client example
'''
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
'''
import asyncio
async def tcp_echo_client(message, loop):
	reader, writer = await asyncio.open_connection('127.0.0.1', 8888, loop=loop)
	print('Send: %r' % message)
	writer.write(message.encode())
	data = await reader.read(100)
	print('Received: %r' % data.decode())
	print('Close the socket')
	writer.close()
message = 'Hello Babby!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()