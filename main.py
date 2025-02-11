def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        print_book_report(path, count_words(file_contents), count_letter(file_contents))


def count_words(full_text):
    return len(full_text.split())


def count_letter(full_text):
    lower_text = full_text.lower()
    char_map = {}
    for letter in lower_text:
        if letter in char_map:
            char_map[letter] += 1
        else:
            char_map[letter] = 1
    return char_map


def print_book_report(path, word_count, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    for letter in letter_count:
        if letter.isalpha():
            print(f'The \'{letter}\' character was found {letter_count[letter]} times')
    print("--- End report ---")


main()
