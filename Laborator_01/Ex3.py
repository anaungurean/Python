# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

first_string = input("Type your first string: ")
second_string = input("Type your second string: ")
number_of_occurrences = 0
position = 0

while  first_string in second_string[position:]:
    number_of_occurrences += 1
    position = second_string.index(first_string, position) + len(first_string)

#varianta mai simpla
# number_of_occurrences= second_string.count(first_string)

print("Number of occurrences of the first string in the second: ",number_of_occurrences)

