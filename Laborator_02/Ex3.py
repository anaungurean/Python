#  3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def operations(a, b):
    intersection = [num for num in a if num in b]
    difference_1 = [num for num in a if not (num in b)]
    difference_2 = [num for num in b if not (num in a)]
    reunion = intersection + difference_1 + difference_2
    return intersection,reunion,difference_1,difference_2


def run_tests():
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]

    intersection, reunion, difference_1, difference_2 = operations(a, b)
    assert intersection == [2, 4], "Test failed for intersection"
    assert reunion == [2, 4, 1, 3, 5, 6, 8, 10], "Test failed for reunion"
    assert difference_1 == [1, 3, 5], "Test failed for difference a - b"
    assert difference_2 == [6, 8, 10], "Test failed for difference b - a"
    print("All tests passed!")


run_tests()



