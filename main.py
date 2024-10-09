def main():
    book_path = "books/frankenstein.txt"
    get_report(book_path)

def get_report(path):
    text = get_book_text(path)
    words = get_word_number(text)
    char = get_char_number(text)
    char_sorted = sorted_char(char)
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")

    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End Report ---")


def sorted_char(char):
    sorted_list = []
    for ch in char:
        sorted_list.append({"char": ch, "num": char[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_number(book):
    words = book.split()
    return len(words)

def get_char_number(book):
    char = {}
    
    for letter in book:
        lowered = letter.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1

    return char

main()
