from collections import Counter

def unique_elements_counter(element: str) -> int:
    assert isinstance(element, str), 'Must be a string type of text!'
    count = Counter(element)
    letters_frequency = 0
    for letter, quantity in count.items():
        if quantity == 1:
            letters_frequency += 1
    return letters_frequency


if __name__ == '__main__':
    text = ['qwxqq']
    for element in text:
        print(unique_elements_counter(element))

