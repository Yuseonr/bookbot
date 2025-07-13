# 13 Jul 2025

from stats import get_words_count

from stats import get_char_count

def main():

    book = get_book_text("books/frankenstein.txt")
    words_count = get_words_count(book)
    alphabet_count = get_char_count(book)

    # print(book)
    print(f"{words_count} words found in the document")
    print(alphabet_count)
    

def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()

main()