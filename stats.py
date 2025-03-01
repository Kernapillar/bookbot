def word_counter(str): 
    count = len(str.split())
    return count

def character_counter(str): 
    characters = {}
    for char in str: 
        char = char.lower()
        if char in characters: 
            characters[char] += 1
        else: 
            characters[char] = 1
    return characters

def sort_key(dict): 
    return dict["count"]

def sorted_output(counts):
    sorted = []
    for key in counts: 
        if key.isalpha():
            sorted.append({"key": key, "count": counts[key]})

    sorted.sort(reverse=True, key=sort_key)
    return sorted