# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

rows = 4
columns = 4

matrix = [
    ["f", "i", "r", "s"],
    ["n", "_", "l", "t"],
    ["o", "b", "a", "_"],
    ["h", "t", "y", "p"]
]

# Initialize variables
string = ""
top_row = 0
bottom_row = rows - 1
left_column = 0
right_column = columns - 1

while top_row <= bottom_row and left_column <= right_column:

    for i in range(left_column, right_column + 1):
        string += matrix[top_row][i]

    top_row += 1

    for i in range(top_row, bottom_row + 1):
        string += matrix[i][right_column]

    right_column -= 1

    if top_row <= bottom_row:
        for i in range(right_column, left_column - 1, -1):
            string += matrix[bottom_row][i]

        bottom_row -= 1

    if left_column <= right_column:
        for i in range(bottom_row, top_row - 1, -1):
            string += matrix[i][left_column]

        left_column += 1

print(string)


