from stats import get_num_words, get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_characters(book_text)
    print(f"{num_words} words found in the document.")
    
    for k, v in num_chars.items():
        print(f"'{k}': {v}")

main()