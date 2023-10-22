# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def fib (n):
    x = 0
    y = 1
    l = list()
    for i in range ( 1 , n+1 ) :
        if i == 1:
            l.append(x)
        elif i == 2 :
            l.append(y)
        else :
            l.append( x + y)
            x, y = y, x + y
    return l


def run_tests():
    assert fib(5) == [0, 1, 1, 2, 3], "Test failed for n=5"
    assert fib(6) == [0, 1, 1, 2, 3, 5], "Test failed for n=6"
    assert len(fib(22)) == 22, "Test failed for n=22"
    assert fib(0) == [], "Test failed for n=0"
    assert fib(1) == [0], "Test failed for n=1"
    assert fib(-1) == [], "Test failed for n=-1"

    print("All tests passed!")


run_tests()

