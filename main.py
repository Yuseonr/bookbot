# 13 Jul 2025

def main():
    print(get_book_text("books/frankenstein.txt"))


def get_book_text(file_path):
    with open (file_path) as f:
        return f.read()


main()