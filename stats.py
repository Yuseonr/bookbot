# 13 Jul 2025

def get_words_count(file_string):
    return len(file_string.split())

def get_char_count(file_string):
    char_dict = {} 
    for char in file_string.lower():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def get_sort_char_count(char_count_dict) :
    list_of_char_dict = []
    for i in char_count_dict :
        char_d = {}
        char_d['char'] = i
        char_d['num'] = char_count_dict[i]
        list_of_char_dict.append(char_d)
    list_of_char_dict.sort(reverse=True, key=lambda x: x['num'])
    return list_of_char_dict

