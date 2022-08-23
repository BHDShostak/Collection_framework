from collections import Counter


def counter_dict(text) -> str:
    count = Counter()
    for letter in text:
        count[letter] += 1
    return count


def unique_number(text) -> str:
    sum_min_quantity = 0
    for letter, quantity in counter_dict(text).items():
        if quantity == 1:
            sum_min_quantity += 1
    return sum_min_quantity


if __name__ == '__main__':
    text = "abbbccdfhytrk"
    print(unique_number(text))

