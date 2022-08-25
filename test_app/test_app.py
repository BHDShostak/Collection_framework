from app.app import unique_elements_counter
import pytest


@pytest.mark.parametrize(
    "text, result, error",
    [
        ("qwxqq", 2, False),
        (121321, None, True),
        (12.1321, None, True),
        ([], None, True),
    ]
)

def test_case(text, result, error):
    if error:
        with pytest.raises(AssertionError):
            unique_elements_counter(text)
    else:
        assert unique_elements_counter(text) == result





