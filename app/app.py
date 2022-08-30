from collections import Counter
from functools import cache


@cache
def count_unique_symbols(symbol: str) -> int:
    assert isinstance(symbol, str), 'Must be a string type of text!'
    letters_frequency = len([value for value in Counter(symbol).values() if value == 1])
    return letters_frequency


if __name__ == '__main__':
    text = ['qwxqq']
    for symbol in text:
        print(count_unique_symbols(symbol))
