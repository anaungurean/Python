#   4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer).
#   The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
#	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose_song(notes, moves, start_position):
    if start_position in range (0,len(notes)) or start_position in range(-len(notes), 0):
        if len(notes) == 0:
            return []
        song = list()
        song.append(notes[start_position])
        next_position = start_position
        for move in moves:
            next_position = (next_position + move) % len(notes)
            song.append(notes[next_position])
        return song
    else:
        return []

def test_compose_song():
    result = compose_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    assert result == ["mi", "fa", "do", "sol", "re"]

    result = compose_song([], [1, -3, 4, 2], 0)
    assert result == []

    result = compose_song(["do", "re", "mi", "fa", "sol"], [], 2)
    assert result == ["mi"]

    result = compose_song(["do", "re", "mi", "fa", "sol"], [1, -1, 1, -1], 4)
    assert result == ['sol', 'do', 'sol', 'do', 'sol']

    print("All tests passed!")


test_compose_song()


