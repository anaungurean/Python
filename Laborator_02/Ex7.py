# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.

def palindrome_numbers(lst):
    counter = 0
    greatest = None
    for elem in lst:
        if elem >= 0:
            elem_string = str(elem)
            if elem_string == elem_string[::-1]:
                counter += 1
                if greatest is None or elem > greatest:
                    greatest = elem

    if greatest is None:
        return(0,None)

    return(counter, greatest)

def test_palindrome_numbers():
    assert palindrome_numbers([-121, 123, 444.87, -454, 0, 9, -11,1.10]) == (3, 9), "Test 1 Failed"  # -121 is now not considered
    assert palindrome_numbers([]) == (0, None), "Test 2 Failed"
    assert palindrome_numbers([123, 456, 789]) == (0, None), "Test 3 Failed"
    assert palindrome_numbers([1, 2, 3, 4, 5]) == (5, 5), "Test 4 Failed"
    assert palindrome_numbers([-11, -22, -33, -44, -55]) == (0, None), "Test 5 Failed"
    assert palindrome_numbers([121]) == (1, 121), "Test 6 Failed"
    print("All Tests Passed!")

test_palindrome_numbers()
