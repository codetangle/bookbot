def get_num_words(text):
    words_array = text.split()
    return len(words_array)

def get_num_characters(text):
    char_count = {}
    for char in text:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count