# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

first_string = input("Type your first string: ")
second_string = input("Type your second string: ")
number_of_occurrences = 0
position = 0

while True:
    found_position = second_string.find(first_string, position)
    if found_position != -1:
        number_of_occurrences += 1
        position = found_position + 1
    else:
        break



print("Number of occurrences of the first string in the second:", number_of_occurrences)


