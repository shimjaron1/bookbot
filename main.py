from stats import word_count
from stats import char_count
from stats import sort_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    txt_file = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count(txt_file)
    print("--------- Character Count -------")

    char_counts = char_count(txt_file)
    sorted_counts=sort_count(char_counts)

    for char in sorted_counts:
        letter = char.get("char")
        count = char["num"]
        print(f"{letter}: {count}")

main()