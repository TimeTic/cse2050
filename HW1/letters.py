import string


def count_letters(file):
    """To count the number of letters in a file."""
    with open(file, 'r') as f:
        text = f.read().lower()
    letter_count = {letter: text.count(letter)
                    for letter in string.ascii_lowercase
                    if letter in text}
    return letter_count


print(count_letters('frost.txt'))
