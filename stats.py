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

def get_char_count_sort_key(char_count):
    return char_count["num"]

def sort_char_count(char_dict):
    list_to_sort = []
    # convert to list of dicts
    for k, v in char_dict.items():
        list_to_sort.append({"char": k, "num": v})

    # sort the list
    list_to_sort.sort(reverse=True, key=get_char_count_sort_key)

    return list_to_sort