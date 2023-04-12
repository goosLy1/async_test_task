import pytest

from settings import TEST_HASH
from downloader.__main__ import get_hash

def test_get_hash(create_test_file):
    assert TEST_HASH == get_hash(create_test_file)



