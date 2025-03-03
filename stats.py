def get_words_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    character_count = {}
    words = text.split()

    for word in words:
        for character in word.lower():
            if character in character_count:
                character_count[character] = character_count[character] + 1
            else:
                character_count[character] = 1
    
    return character_count
