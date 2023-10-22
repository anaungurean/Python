# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def is_prime(x):
    if x < 2:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True


def find_prime_numbers(numbers):

    prime_numbers = [number for number in numbers if is_prime(number)]
    return prime_numbers


def run_tests():
    assert find_prime_numbers([13, 6, 61, 19, 34, 31]) == [13, 61, 19,31]
    assert find_prime_numbers([2, 7, 1, 0, 3442,7919 ]) == [2, 7, 7919]
    assert find_prime_numbers([]) == []
    assert find_prime_numbers([0, 1, 4, 6, 8, 9]) == []
    print("All tests passed!")


run_tests()
