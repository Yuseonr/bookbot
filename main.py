# 13 Jul 2025

def main():

    book = get_book_text("books/frankenstein.txt")
    words_count = get_words_count(book)

    # print(book)

    print(f"{words_count} words found in the document")
    

def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()

def get_words_count(file_string):
    return len(file_string.split())


main()