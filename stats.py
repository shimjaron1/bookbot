def word_count(txt_file):
    words = len(txt_file.split())
    
    return print(f"Found {words} total words")

def char_count(txt_file):
    char_list = list(txt_file.lower())
    char_counts = {}
    for char in char_list:
        count = char_counts.get(char,0)+1
        char_counts.update({char:count})
    #return print(char_counts)
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_count(char_counts):
    sorted = []
    for char in char_counts:
        if char.isalpha() is True:
            count = char_counts.get(char)
            sorted.append({"char":char, "num": count})

    sorted.sort(reverse=True, key=sort_on)
    return sorted