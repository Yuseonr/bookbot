# 13 Jul 2025

import sys
from stats import get_words_count
from stats import get_char_count
from stats import get_sort_char_count

def main():
    path = sys.argv[1]
    book = get_book_text(path)
    words_count = get_words_count(book)
    char_count_dict = get_char_count(book)
    sort_char_count = get_sort_char_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    show_char_count(sort_char_count)
    print("============= END ===============")
        

def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()

def show_char_count (sorted_char_count):
    for i in range (len(sorted_char_count)):
        if sorted_char_count[i]['char'].isalpha() :
            print(f"{sorted_char_count[i]['char']}: {sorted_char_count[i]['num']}")


if len(sys.argv) == 2 :
    main()
else :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)