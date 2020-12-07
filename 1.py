import asyncio
import time

async def say_after(delay, what):
	while True :
	    await asyncio.sleep(delay)
	    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(4, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    task3 = asyncio.create_task(
        say_after(2, 'hoppa'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())