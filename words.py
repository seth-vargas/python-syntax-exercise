def print_upper_words(words, starting_letter):
    """ Converts string to uppercase"""

    for word in words:
        word = word.upper()
        for letter in starting_letter:
            letter = letter.upper()
            if word.startswith(letter):
                print(word.upper())
                break

print(print_upper_words(["Hello", "Goodbye"], ["l", "g"]))
