import functools

from app.app import count_unique_symbols
import pytest
import functools

@pytest.mark.parametrize(
    "text, result",
    [
        ("qwxqq", 2),
        ("qw11d12xqq", 4),
    ]
)
def test_case1(text, result):
    assert count_unique_symbols(text) == result

@functools.lru_cache(maxsize=None)
    def test_cache_case(text: str) -> int:
        return count_unique_symbols(text)


@pytest.mark.parametrize(
    "text",
    [
        (121321, None),
        (12.1321, None),
    ]
)
def test_case2(text):
    with pytest.raises(AssertionError):
        count_unique_symbols(text)


