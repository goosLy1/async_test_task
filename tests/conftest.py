import os
import pytest
import aiohttp


@pytest.fixture()
def create_test_file():
    filename = "testfile.txt"
    with open(filename, "w") as file:
        file.write("12345678qwerty")  
    yield filename
    os.remove(filename)


@pytest.fixture()
async def create_session():
    async with aiohttp.ClientSession() as session:
          yield session
