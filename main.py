def get_book_text(filepath): 
    with open(filepath) as f: 
        file_contents = f.read()
        return file_contents

def word_counter(str): 
    count = len(str.split())
    print(f"{count} words found in the document")

def main(): 
    word_counter(get_book_text("./books/frankenstein.txt") )

main()