# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example:
# ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def test_sort_tuples():
    assert sort_tuples([('abc', 'bcd'), ('abc', 'zza')]) == [('abc', 'zza'), ('abc', 'bcd')]
    assert sort_tuples([('abc', 'xyz'), ('ghi', 'ab'), ('def', 'uvwxy')]) == [('ghi', 'ab'), ('def', 'uvwxy'), ('abc', 'xyz')]
    assert sort_tuples([('abc', 'aaa'), ('ghi', 'bbb'), ('def', 'ccc')]) == [('abc', 'aaa'), ('ghi', 'bbb'), ('def', 'ccc')]
    assert sort_tuples([]) == []
    assert sort_tuples([('abc', 'xyz')]) == [('abc', 'xyz')]
    assert sort_tuples([('abc', 'abc'), ('def', 'def')]) == [('abc', 'abc'), ('def', 'def')]
    print("All tests passed!")

def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1][2] if len(x[1]) > 2 else "")


test_sort_tuples()


