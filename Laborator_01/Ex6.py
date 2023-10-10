# Write a function that validates if a number is a palindrome.

def check_palindrome (number) :
    ogl = 0
    aux = number
    while aux > 0:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10

    if ogl == number :
        print (f"The number {number} is a palindrome")
    else :
        print (f"The number {number } is not a palindrome")

#varianta mai smechera
def check_palindrome_2 (number) :

    number_string = str(number)
    if number_string == number_string[::-1] :
        print (f"The number {number} is a palindrome")
    else :
        print (f"The number {number } is not a palindrome")


check_palindrome_2(123121)
check_palindrome_2(123321)