# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def modify_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return []
    for index_row, row in enumerate(matrix):
        for index_column, element in enumerate(row):
            if index_row > index_column:
                row[index_column] = 0
    return matrix


print(modify_matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))

