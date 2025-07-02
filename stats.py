
def num_words(file_contents):
    words = file_contents.split()
    len_words = len(words)
    return len_words

def character_count(file_contents):
    lowercase_text = file_contents.lower()
    all_letters = list(lowercase_text)
    letter_count = {}
    for letter in all_letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def sorted_list(letter_count):
    def sort_on(letters):
        return letters["num"]
    result = []
    letter_list = [{"char": key,"num": value} for key, value in letter_count.items()]
    letter_list.sort(reverse=True, key=sort_on)
    for letter in letter_list:
        if letter["char"].isalpha():
            result.append(f"{letter['char']}: {letter['num']}")
    return result

