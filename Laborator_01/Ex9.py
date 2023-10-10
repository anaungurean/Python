# Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a"
# represent the same character.

def most_common_character (string):

    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    most_common=''
    max_count=0

    for char in alphabet:
        count = string.count(char)
        if count > max_count:
            most_common = char
            max_count = count
    print(f"The most common letter in the text is {most_common}, that appears of {max_count} times")

most_common_character("an apple is not a tomato")

