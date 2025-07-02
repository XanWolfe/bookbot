import sys

def process_arguments():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents


def main():
    process_arguments()
    from stats import num_words
    from stats import character_count
    from stats import sorted_list
    book_text = get_book_text(sys.argv[1])
    number_of_characters = sorted_list(character_count(book_text))
    word_count = num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for line in number_of_characters:
        print(line)
    print("============= END ==============")

main()