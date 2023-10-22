# Write a function that receives a variable number of lists and returns a lst of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.
# Example: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]
# Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.

def test_generates_tuples():
    assert generates_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"]) == [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c')]
    assert generates_tuples([1, 2], [3, 4], [5, 6]) == [(1, 3, 5), (2, 4, 6)]
    assert generates_tuples([1], [2], [3]) == [(1, 2, 3)]
    assert generates_tuples([1, 2, 3], [], [4, 5]) == [(1, None, 4), (2, None, 5), (3, None, None)]
    assert generates_tuples() == []
    assert generates_tuples([1, 2, 3]) == [(1,), (2,), (3,)]
    assert generates_tuples([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]) == [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
    print("All tests passed!")


def generates_tuples(*lists):
    if len(lists) == 0:
        return []

    number_of_lists = max([len(x) for x in lists])
    generated_list = list()
    for index in range(number_of_lists):
        t = tuple(lst[index] if index < len(lst) else None for lst in lists)
        generated_list.append(t)
    return generated_list


test_generates_tuples()



