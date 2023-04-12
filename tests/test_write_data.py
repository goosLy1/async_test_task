import pytest
import filecmp

from downloader.__main__ import write_data


@pytest.mark.asyncio
async def test_write_data(mocker, create_test_file):
    mocker.patch("downloader.__main__.get_data", return_value = "12345678qwerty")
    result = await write_data('','','')
    assert filecmp.cmp(result, create_test_file, shallow=False)