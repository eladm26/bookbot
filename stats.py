from collections import defaultdict
import typing


def get_number_of_words(book_content: str) -> int:
    num_of_words = len(book_content.split())
    return num_of_words

def get_chars_count(book_content: str) -> dict[str, int]:
    chars_count = defaultdict(int)
    for c in book_content:
        chars_count[c.lower()] += 1

    return chars_count

def create_count_dicts(chars_count: dict[str, int]) -> list[dict[str, typing.Any]]:
    res = []
    for c, n in chars_count.items():
        res.append({'char': c, 'num': n})

    res.sort(key=lambda pair: pair['num'], reverse=True)
    return res
