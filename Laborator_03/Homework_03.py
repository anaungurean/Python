'''
Ex1. Write a function that receives as parameters two lists a and b
and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
'''


def ex_01(a, b):
    set_1 = set(a)
    set_2 = set(b)
    intersection = set_1.intersection(set_2)  # set_1 & set_2
    union = set_1.union(set_2)  # set_1 | set_2
    difference_1 = set_1.difference(set_2)  # set_1 - set_2
    difference_2 = set_2.difference(set_1)  # set_2 - set_1
    all_operations = [intersection, union, difference_1, difference_2]
    return all_operations


'''
Ex2. Write a function that receives a string as a parameter and returns a dictionary in
which the keys are the characters in the character string and the values are the number
of occurrences of that character in the given text. 
Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
'''


def ex_02(string):
    d = {}  # d = dict()
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    # d = {char : str.count(char) for char in str} --> less efficient?
    return d


'''
Compare two dictionaries without using the operator "==" returning True or False. 
(Attention, dictionaries must be recursively covered because they can contain other containers,
 such as dictionaries, lists, sets, etc.)
'''


def lists_are_equal(l1, l2):
    if len(l1) != len(l2):
        return False

    l2_copy = l2.copy()

    for elem in l1:
        if elem in l2_copy:
            l2_copy.remove(elem)
        else:
            return False
    return True


def sets_are_equal(s1, s2):
    def is_subset(small_set, large_set):
        for elem in small_set:
            if elem not in large_set:
                return False
        return True

    return is_subset(s1, s2) and is_subset(s2, s1)


def tuples_are_equal(t1, t2):
    if len(t1) != len(t2):
        return False

    for elem1, elem2 in zip(t1, t2):
        if elem1 != elem2:
            return False

    return True


def ex_03(d1, d2):
    if len(d1) != len(d2):
        return False
    else:
        for i in d1.keys():
            if i not in d2:
                return False
            else:
                if type(d1[i]) != type(d2[i]):
                    return False
                else:
                    if isinstance(d1[i], dict):
                        if ex_03(d1[i], d2[i]) is not True:
                            return False
                    elif isinstance(d1[i], list):
                        if lists_are_equal(d1[i], d2[i]) is not True:
                            return False
                    elif isinstance(d1[i], set):
                        if sets_are_equal(d1[i], d2[i]) is not True:
                            return False
                    elif isinstance(d1[i], tuple):
                        if tuples_are_equal(d1[i], d2[i]) is not True:
                            return False
                    else:
                        if d1[i] != d2[i]:
                            return False
    return True


'''
Ex4. The build_xml_element function receives the following parameters:
tag, content, and key-value elements given as name-parameters. 
Build and return a string that represents the corresponding XML element. 
Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "
'''


def ex_04(tag, content, **attrs):
    xml_element = "<" + tag
    for key, value in attrs.items():
        if key.startswith("_"):
            key = key.replace("_", "", 1)
        xml_element += f' {key}="{value}"'

    xml_element += ">" + content
    if tag != "img":
        xml_element += f"</{tag}>"

    return xml_element


'''
Ex5. The validate_dict function that receives as a parameter a set of tuples
( that represents validation rules for a dictionary that has strings as keys and values)
and a dictionary. A rule is defined as follows:
(key, "prefix", "middle", "suffix").
A value is considered valid if it starts with 
"prefix", "middle" is inside the value
(not at the beginning or end) and ends with "suffix".
The function will return True if the given dictionary matches all the rules, False otherwise.
Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} 
and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False
because although the rules are respected for "key1" and "key2" "key3" 
that does not appear in the rules.
'''


def find_rule(rules, key):
    for rule in rules:
        if rule[0] == key:
            return rule
    return None


def verify_middle(value, middle):
    if middle:
        if middle not in value:
            return False
        start_index = value.find(middle)
        end_index = start_index + len(middle)
        if middle == value:
            return True
        if start_index == 0 or end_index == len(value):
            return False
    return True


def ex_05(rules, dictionary):
    for key, value in dictionary.items():
        rule = find_rule(rules, key)
        if rule is None:
            return False
        prefix, middle, suffix = rule[1], rule[2], rule[3]
        if not value.startswith(prefix) or not value.endswith(suffix):
            return False

        value_without_pref_suf = value[len(prefix):-len(suffix)] if suffix else value[len(prefix):]
        if suffix != "" and prefix != "":
            if middle not in value_without_pref_suf:
                return False
        else:
            if not verify_middle(value_without_pref_suf, middle):
                return False

    return True


'''
Ex.6 Write a function that receives as a parameter
a list and returns a tuple (a, b), representing the number of
unique elements in the list, and b representing the number of 
duplicate elements in the list (use sets to achieve this objective).
'''


def ex_06(lst):
    my_set = set(lst)
    my_tuple = (len(my_set), len(lst) - len(my_set))
    return my_tuple


'''
Ex7.Write a function that receives a variable number of sets and returns a dictionary
with the following operations from all sets two by two: reunion, intersection, a-b, b-a.
The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. Ex:
{1,2}, {2, 3} =>
{
    "{1, 2} | {2, 3}":  {1, 2, 3},
    "{1, 2} & {2, 3}":  { 2 },
    "{1, 2} - {2, 3}":  { 1 },
    ...
}
'''


def ex_07(*args):
    d = {}
    for index_1, set_1 in enumerate(args):
        for index_2 in range(index_1 + 1, len(args)):
            set_2 = args[index_2]
            key = f"{set_1 if set_1 else '{}'} | {set_2 if set_2 else '{}'}"
            d[key] = set_1.union(set_2)
            key = f"{set_1 if set_1 else '{}'} & {set_2 if set_2 else '{}'}"
            d[key] = set_1.intersection(set_2)
            key = f"{set_1 if set_1 else '{}'} - {set_2 if set_2 else '{}'}"
            d[key] = set_1.difference(set_2)
            key = f"{set_2 if set_2 else '{}'} - {set_1 if set_1 else '{}'}"
            d[key] = set_2.difference(set_1)
    return d


'''
Ex8.Write a function that receives a single dict parameter named mapping. 
This dictionary always contains a string key "start".
Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: 
the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
The function must return the list of objects obtained as previously described. Ex:
loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
'''


def ex_08(mapping: dict) -> list:
    visited_key = ['start']
    key = mapping['start']
    while key not in visited_key:
        visited_key.append(key)
        key = mapping[key]
    return visited_key[1:]


'''
Ex.9 Write a function that receives a variable number of positional arguments
and a variable number of keyword arguments and will return the number of positional arguments
whose values can be found among keyword arguments values. Ex:
my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
'''


def ex_09(*args, **kwargs):
    count = 0
    for val in args:
        if val in kwargs.values():
            count += 1
    return count



            




