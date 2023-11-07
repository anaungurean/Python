'''
Ex1. Write a Python class that simulates a Stack.
The class should implement methods like push, pop, peek
(the last two methods should return None if no element is present in the stack).
'''
import copy

class Stack:

    def __init__(self):
        self.__items = []

    def get_size(self):
        return len(self.__items)

    def is_empty(self):
        return self.get_size() == 0

    def push(self, item: object):
        item_copy = copy.deepcopy(item)
        self.__items.append(item_copy)

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            return self.__items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            if not isinstance(self.__items[-1], (int, float, str, bool, tuple)):
                item = copy.deepcopy(self.__items[-1])
            else:
                item = self.__items[-1]
            return item

    def __str__(self):
        return str(self.__items)


'''
Ex2. Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek 
(the last two methods should return None if no element is present in the queue).
'''


class Queue:

    def __init__(self):
        self.__items = []

    def get_size(self):
        return len(self.__items)

    def is_empty(self):
        return self.get_size() == 0

    def push(self, item: object):
        item_copy = copy.deepcopy(item)
        self.__items.append(item_copy)

    def pop(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        else:
            return self.__items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        else:
            if not isinstance(self.__items[0], (int, float, str, bool, tuple)):
                item = copy.deepcopy(self.__items[0])
            else:
                item = self.__items[0]
            return item

    def __str__(self):
        return str(self.__items)

'''
Ex03. Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
The class should provide methods to access elements (get and set methods) and some mathematical functions 
such as transpose, matrix multiplication and a method that allows iterating through all elements 
form a matrix an apply a transformation over them (via a lambda function).
'''

class Matrix:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__matrix = [[0 for column in range(columns)] for row in range(rows)]

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, matrix):
        if len(matrix) != self.__rows or len(matrix[0]) != self.__columns:
            raise ValueError("Matricea dată ca parametru nu are dimensiunile corecte.")

        for row in matrix:
            if len(row) != self.__columns:
                raise ValueError("Unul dintre rânduri nu are dimensiunea corectă.")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("Toate elementele matricei trebuie să fie int sau float.")
        self.__matrix = matrix

    def get_element(self, row, column):
        return self.__matrix[row][column]

    def set_element(self, row, column, value):
        if row < 0 or row >= self.__rows or column < 0 or column >= self.__columns:
            raise ValueError("Coordonatele date nu sunt valide")

        if not isinstance(value, (int, float)):
            raise TypeError("Elementul trebuie să fie un număr întreg sau un număr real.")

        self.__matrix[row][column] = value

    def transpose(self):
        new_matrix = Matrix(self.__columns, self.__rows)
        for row in range(self.__rows):
            for column in range(self.__columns):
                new_matrix.set_element(column, row, self.get_element(row, column))
        return new_matrix

    def __mul__(self, other):
        if self.__columns != other.get_rows():
            raise Exception("Numarul de coloane a primei matrici trebuie sa fie egal cu numarul de linii ale celeilalte matrici")
        else:
            result_matrix = Matrix(self.__rows, other.get_columns())
            for row in range(0, self.__rows):
                for column in range(0, other.get_columns()):
                    value = 0
                    for i in range(0, self.__columns):
                        value += self.get_element(row, i) * other.get_element(i, column)
                    result_matrix.set_element(row, column, value)
            return result_matrix

    def apply(self, function):
        for row in range(0, self.__rows):
            for column in range(0, self.__columns):
                try:
                    value = function(self.get_element(row, column))
                    self.set_element(row, column, value)
                except Exception as e:
                    raise Exception("Nu s-a putut aplica funcția pe elementul de pe linia " + str(row) + " și coloana " + str(column) + ". Cauza: " + str(e))

    def __str__(self):
        matrix_str = ""
        for row in self.__matrix:
            matrix_str += ' '.join(map(str, row)) + "\n"
        return matrix_str


