def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == row - i:
            return False
    return True


def bfs(start,n):
    q=[[start]]
    while q:
        board=q.pop(0)
        if len(board)==n:
            return board
        row = len(board)
        for col in range(n):
            if isSafe(board,row,col):
                q.append(board+[col])            
n=8
print(bfs(2,8))

