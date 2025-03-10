def get_words_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    character_count = {}

    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    return character_count

def sort_dictionaries(dict: dict[str, int]) -> list[dict[str, int]]:
    sorted_list_of_dicts = []
    for key, value in dict.items():
        sorted_list_of_dicts.append({"character": key, "count": value})

    sorted_list_of_dicts.sort(reverse=True, key=sort_on)
    return sorted_list_of_dicts

def sort_on(dict: dict[str, int]) -> int:
    return dict["count"]