# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.

def count_words (text):
    words = text.split(" ")
    return len(words)

print(count_words("I have Python exam"))
