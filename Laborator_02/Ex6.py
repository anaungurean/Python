# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def counting(x, *lists):
    numbers_x_times = list()
    for l in lists:
        for elem in l:
            if elem not in numbers_x_times:
                counter = sum(l2.count(elem) for l2 in lists)
                if counter == x:
                    numbers_x_times.append(elem)
    return numbers_x_times


print(counting(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
print(counting(-1, [1, 2, 3], [1, 2]))
print(counting(1, [1, 2], ["1"], [1, 0]))
