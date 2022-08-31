import functools
from app.app import count_unique_symbols
import pytest


count_unique_symbols.cache_clear()
@pytest.mark.parametrize(
    "text, result",
    [
        ("qwxqq", 2),
        ("qw11d12xqq", 4),
    ]
)

@functools.lru_cache
def test_case1(text, result):
    assert count_unique_symbols(text) == result
    print(count_unique_symbols.cache_info())

@pytest.mark.parametrize(
    "text",
    [
        (121321),
        (12.1321),
        ((1, 2)),
        (None),
        (True),
        (False),
        (b'''Python Tutorial''')
    ]
)
@functools.lru_cache
def test_case2(text):
    with pytest.raises(AssertionError):
        count_unique_symbols(text)
    print(count_unique_symbols.cache_info())


