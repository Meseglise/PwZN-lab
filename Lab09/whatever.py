import asyncio
import time


async def hello_async():
    # await asyncio.sleep(5)
    time.sleep(5)
    print('Hello Async World!')
    return 'YOLO'


async def main():
    # tasks = [asyncio.create_task(hello_async()) for _ in range(4)]

    # await asyncio.gather(*tasks)

    # for task in tasks:
    #     await task

    print(await asyncio.gather(*[hello_async() for _ in range(4)]))


asyncio.run(main())