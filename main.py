from stats import get_num_words, get_num_characters, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_character_count(char_count_list):
    for count_dict in char_count_list:
        char = count_dict["char"]
        count = count_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
        
def print_report(number_words, char_count_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")
    print_character_count(char_count_list)
    print("============= END ===============")
    
def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_characters(book_text)
    sorted_char_count = sort_char_count(num_chars)
    
    print_report(num_words, sorted_char_count)

main()