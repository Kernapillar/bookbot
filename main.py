from stats import word_counter, character_counter, sorted_output
from sys import argv, exit

def get_book_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read()
        return file_contents
    
def formatted_output(word_count, sorted_counts, path):
    neat_sorted_counts = "\n"
    for pair in sorted_counts: 
        neat_sorted_counts += f"{pair["key"]}: {pair["count"]} \n"
    return f"""============ BOOKBOT ============ \n
    Analyzing book found at {path}... \n
    ----------- Word Count ---------- \n
    Found {word_count} total words \n
    --------- Character Count ------- \n
    {neat_sorted_counts} 
    ============= END ===============

    """
def main(): 
    if len(argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    path = argv[1]
    text = get_book_text(path)
    count = word_counter(text)
    sorted = sorted_output(character_counter(text))
    print(formatted_output(count, sorted, path))

main()