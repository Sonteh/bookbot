from stats import get_words_count, get_character_count

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    words_count = get_words_count(file_contents)
    character_count = get_character_count(file_contents)
    print(f"{words_count} words found in the document")
    print(f"{character_count}")

main()