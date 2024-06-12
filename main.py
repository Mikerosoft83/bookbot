def main():
    path= "books/frankenstein.txt"
    text = get_text(path)
    num_words = word_count(text)
    num_chars = char_count(text)
    org = organize_dict(num_chars)
    
    print(f"--- Start report on {path} ---")
    print()
    print(f"{num_words} words found in the book")
    print()

    for item in org:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['number']} times")
    print()
    print("--- End of report ---")

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    l_words = text.lower()
    letters = {}
    for l in l_words:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def get_text(path):
    with open(path) as p:
        return p.read()
    
def sort_on(s):
    return s["number"]
    
def organize_dict(num_chars):
    sorted = []
    for char in num_chars:
        sorted.append({"letter": char, "number": num_chars[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


main()
