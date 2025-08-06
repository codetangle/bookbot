def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_number_of_words(text):
    words_array = text.split()
    return len(words_array)
    
def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    number_of_words = get_number_of_words(book_text)
    print(f"{number_of_words} words found in the document.")

main()