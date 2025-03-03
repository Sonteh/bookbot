def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()

def get_words_count(text: str) -> int:
    return len(text.split())

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    words_count = get_words_count(file_contents)
    print(f"{words_count} words found in the document")

main()