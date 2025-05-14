def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()  # Convert entire string to lowercase
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def final_sort(char_dict):
    result = []
    for char, num in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            result.append({"char": char, "num": num})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result