import string
def count_letters(file):
    """To count the number of letters in a file."""
# opening files and readin it
    with open(file, 'r') as f:
        text = f.read().lower()
# counting letters
    letter_count = {letter_char: text.count(letter_char)
                    for letter_char in string.ascii_lowercase 
                    if letter_char in text}
    return letter_count
# print letters
print(count_letters())
