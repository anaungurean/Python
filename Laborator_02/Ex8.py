# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def ascii_code_divisible_by_x(lst, x=1, flag=True):
    l1 = list()
    for string in lst:
        l2 = list()
        for char in string:
            if flag is True and ord(char) % x == 0:
                l2.append(char)
            elif flag is False and ord(char) % x != 0:
                l2.append(char)
        if len(l2) > 0:
            l1.append(l2)
    return l1

print(ascii_code_divisible_by_x(["test", "hello", "lab002"], 2, False))







