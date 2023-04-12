import os

import aiohttp
import asyncio
import aiofiles
import hashlib
import tempfile
import collections
from time import time

from settings import URL


async def write_data(url: str, session: aiohttp.ClientSession, temp_dir: str) -> str:
    response_data = await get_data(url, session)
    filename = os.path.join(temp_dir, "filename-{}.txt".format(int(time() * 1000)))  
    
    async with aiofiles.open(filename, mode="wt") as file:
        await file.write(response_data)
    return filename


async def get_data(url: str, session: aiohttp.ClientSession) -> str:
    async with session.head(url) as response:
        if response.status != 200:
            raise aiohttp.ClientError()
        return str(response.headers)
        
        
# async def get_hash(filename: str) -> str:
#      async with aiofiles.open(filename, 'r') as f:
#             data = await f.read()
#             sha256hash = hashlib.sha256(data.encode()).hexdigest()
#             print(sha256hash)
#             return sha256hash


def get_hash(filename: str) -> str:
    with open(filename, "r") as file:
        file_data = file.read()
        sha256hash = hashlib.sha256(file_data.encode()).hexdigest()
        print(sha256hash)
        return sha256hash


async def main():
    tasks = collections.deque()
    async with aiohttp.ClientSession() as session:

        with tempfile.TemporaryDirectory() as temp_dir:

            for _ in range(3):
                task = asyncio.create_task(write_data(URL, session, temp_dir))
                tasks.append(task)

            func_results = await asyncio.gather(*tasks, return_exceptions=True)
            for filename in func_results:
                get_hash(filename)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
