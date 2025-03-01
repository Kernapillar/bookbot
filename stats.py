def word_counter(str): 
    count = len(str.split())
    print(f"{count} words found in the document")

def character_counter(str): 
    characters = {}
    for char in str: 
        char = char.lower()
        if char in characters: 
            characters[char] += 1
        else: 
            characters[char] = 1
    return characters