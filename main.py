import sys
from stats import get_number_of_words, get_chars_count, create_count_dicts


def get_book_test(filename: str) -> str:
    with open(filename) as f:
        file_content = f.read()

    return file_content

def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    file_path: str = sys.argv[1]
    file_content = get_book_test(filename=file_path)
    num_words = get_number_of_words(file_content)

    chars_count = get_chars_count(file_content)

    pretty_count = create_count_dicts(chars_count)

    print(f'Found {num_words} total words')
    print(chars_count)
    for pair in pretty_count:
        if pair["char"].isalpha():
            print(f'{pair["char"]}: {pair["num"]}')


if __name__ == '__main__':
    main()
