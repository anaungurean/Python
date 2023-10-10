# Find The greatest common divisor of multiple numbers read from the console.
def find_gcd(a, b):
   if(a == 0) :
       return b
   return find_gcd(b % a, a)

numbers = input("Enter numbers delimited by spaces: ")
string_numbers = numbers.split()
integer_numbers = [int(num) for num in string_numbers]
val1 = integer_numbers[0]
val2 = integer_numbers[1]
gcd = find_gcd(val1,val2)

for i in range(2,len(integer_numbers)):
    gcd = find_gcd (gcd, integer_numbers[i])

print("The greatest common divisor is: ", gcd)



