from stats import word_counter

def get_book_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read()
        return file_contents

def main(): 
    word_counter(get_book_text("./books/frankenstein.txt") )

main()