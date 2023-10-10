# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.

def find_number (text):
    number = ''
    for char in text:
        if char.isdigit():
            number += char
        elif number:
            return int(number)
    if number:
        return int(number)
    else:
        return "Not found"

print(find_number("An apple is 123 USD"))
print(find_number("abc123abc"))
print(find_number("abcabc"))