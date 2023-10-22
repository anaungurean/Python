# Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.
# Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

def test_group_by_rhyme():
    assert group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) == [['ana', 'banana'], ['carte', 'parte'], ['arme']]
    assert group_by_rhyme(['cat', 'dog', 'bat', 'log']) == [['cat', 'bat'], ['dog', 'log']]
    assert group_by_rhyme(['apple', 'orange', 'banana']) == [['apple'], ['orange'], ['banana']]
    assert group_by_rhyme(['apple', 'banana']) == [['apple'], ['banana']]
    assert group_by_rhyme(['apple', 'bapple']) == [['apple', 'bapple']]
    assert group_by_rhyme([]) == []
    assert group_by_rhyme(['apple']) == [['apple']]
    print("All tests passed!")


def group_by_rhyme(lst):
    lst1 = list()
    used_words = list()
    for string in lst:
        if string not in used_words:
            lst2 = list()
            for index in range (lst.index(string),len(lst)):
                string2 = lst[index]
                if string2 not in lst1:
                    if string[-2::] == string2[-2::]:
                        lst2.append(string2)
                        used_words.append(string2)
            lst1.append(lst2)
    return lst1


test_group_by_rhyme()
