# 13 Jul 2025

def get_words_count(file_string):
    return len(file_string.split())

def get_char_count(file_string):
    char_dict = {} 
    for char in file_string.lower():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

   
