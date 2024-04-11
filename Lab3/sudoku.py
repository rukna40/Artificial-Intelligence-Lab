def is_valid(board,num):
    for i in board:
        for j in i:
            if num==j:
                return False




sudoku_board = [
    [0, 0, 3],
    [1, 0, 0],
    [0, 0, 2]
]