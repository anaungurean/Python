# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list
# of tuples (line, column) each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him.
# All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field. Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]]
#  Will return : [(2, 2), (3, 4), (2, 4)]


def should_change_seat(matrix):
    if len(matrix) == 0:
        return []
    lst = list()
    for col in range(len(matrix[0])):
        tallest = 0
        for row in range(len(matrix)):
            if matrix[row][col] > tallest:
                tallest = matrix[row][col]
            else:
                lst.append((row, col))
    return lst



def test_should_change_seat():
    # Testul din cerință
    stadium1 = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]
    print (should_change_seat(stadium1) ) #[(2, 2), (3, 4), (2, 4)]

    # Toți spectatorii pot vedea jocul
    stadium2 = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ]
    print (should_change_seat(stadium2)) #[]

    # Nimeni nu poate vedea jocul
    stadium3 = [
        [5, 5, 5],
        [4, 4, 4],
        [3, 3, 3]
    ]
    print (should_change_seat(stadium3))  #[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    # Matrice goală
    stadium4 = []
    print (should_change_seat(stadium4)) #[]

    # Matrice cu un singur rând
    stadium5 = [[1, 2, 3, 2, 1]]
    print (should_change_seat(stadium5))  #[]

    # Matrice cu o singură coloană
    stadium6 = [[1], [2], [3], [2], [1]]
    print (should_change_seat(stadium6)) #[]


test_should_change_seat()

