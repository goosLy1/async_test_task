import pytest
import aiohttp

from downloader.__main__ import get_data
from settings import URL, TEST_URL

   
@pytest.mark.asyncio
async def test_get_data(create_session):
    session = await create_session.__anext__()       
    data = await get_data(URL, session)
    assert 'Accept-Encoding' in data


@pytest.mark.asyncio
async def test_get_data_status(create_session):
    session = await create_session.__anext__()
    with pytest.raises(aiohttp.ClientError):
        await get_data(TEST_URL, session)
    
