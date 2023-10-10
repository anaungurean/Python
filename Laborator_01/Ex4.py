# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

string = input("Type a string in UpperCamelCase: ")
new_string = string[0].lower()

for char in string[1:]:
    if char.isupper():
        new_string += "_" + char.lower()
    else:
        new_string += char.lower()

print("The string in lowercase_with_underscores is: ", new_string)


