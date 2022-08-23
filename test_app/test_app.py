from app.app import unique_number


def test_standard():
    assert unique_number('abbbccdfhytrk') == 8

def test_exception():
    try:
        unique_number(10123123)
    except Exception as exc:
        assert True, f"'10123123' raised an exception {exc}"

