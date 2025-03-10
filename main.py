from stats import get_words_count, get_character_count, sort_dictionaries
import sys

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()

def print_report(book_path, words_count, sorted_list_of_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_dicts:
        if not item["character"].isalpha():
            continue
        print(f"{item["character"]}: {item["count"]}")
            
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    words_count = get_words_count(file_contents)
    character_count = get_character_count(file_contents)
    sorted_list_of_dicts = sort_dictionaries(character_count)
    print_report(book_path, words_count, sorted_list_of_dicts)

main()