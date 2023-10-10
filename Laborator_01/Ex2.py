# Write a script that calculates how many vowels are in a string

string = input("Type your string: ")
number_of_vowels = 0

for i in range (0,len(string)): #for char in string
    if string[i] in "AEIOUaeiou" :
        number_of_vowels +=1


#varianta mai simpla
# number_of_vowels1 = string.count("A") + string.count("A") + string.count("A") + string.count("E") + string.count("I") + string.count("O") + string.count("U") + string.count("a") + string.count("e") + string.count("i") + string.count("u")
print("The number of vowels in your string is:", number_of_vowels)

