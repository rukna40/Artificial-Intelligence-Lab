# import random


# def initialize(n):
#     board = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         board[random.randint(0, n - 1)][i] = 1
#     return board


# def calcCost(board):
#     cost = 0
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 1:
#                 # for k in range(i+1,len(board)):
#                 #     if board[k][j]==1:
#                 #         cost+=1
#                 for k in range(j + 1, len(board)):
#                     if board[i][k] == 1:
#                         cost += 1
#                 a, b = i + 1, j + 1
#                 while a < len(board) and b < len(board):
#                     if board[a][b] == 1:
#                         cost += 1
#                     a += 1
#                     b += 1
#                 a, b = i + 1, j - 1
#                 while a < len(board) and b < len(board):
#                     if board[a][b] == 1:
#                         cost += 1
#                     a += 1
#                     b -= 1
#     return cost


# def find(board):
#     positions=[]
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 1:
#                 positions.append((i, j))
#     return positions

# def move(mat):
#     board = [row[:] for row in mat]
#     positions = find(board)
#     max=float('inf')
#     next=board
#     for pos in positions:
#         x,y=pos
#         row = random.randint(0, len(mat)-1)
#         board[row][y], board[x][y] = board[x][y], board[row][y]
#         cost=calcCost(board)
#         if cost<max:
#             cost=max
#             next=board
#     return next

# def hc(n):
#     board=initialize(n)
#     moves=0
#     path=[board]
#     for i in range(100000):
#         cost=calcCost(board)
#         if cost==0:
#             return path,moves,cost
#         next=move(board)
#         if calcCost(next)<cost:
#             board=next
#             path+=[board]
#             moves+=1
#     return path,moves,cost
    

# path,moves,cost=hc(8)
# for i in path:
#     for j in i:
#         print(j)
#     print()
# print("Moves",moves)
# print("Cost",cost)


import random
import matplotlib.pyplot as plt

def initialize(n):
    board = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        board[random.randint(0, n - 1)][i] = 1
    return board

def calcCost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in range(j + 1, len(board)):
                    if board[i][k] == 1:
                        cost += 1
                a, b = i + 1, j + 1
                while a < len(board) and b < len(board):
                    if board[a][b] == 1:
                        cost += 1
                    a += 1
                    b += 1
                a, b = i + 1, j - 1
                while a < len(board) and b >= 0:
                    if board[a][b] == 1:
                        cost += 1
                    a += 1
                    b -= 1
    return cost

def find(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                positions.append((i, j))
    return positions

def move(mat):
    board = [row[:] for row in mat]
    positions = find(board)
    min_cost = calcCost(board)
    next_board = board
    for pos in positions:
        x, y = pos
        for row in range(len(board)):
            if row != x:
                new_board = [r[:] for r in board]
                new_board[row][y], new_board[x][y] = new_board[x][y], new_board[row][y]
                cost = calcCost(new_board)
                if cost < min_cost:
                    min_cost = cost
                    next_board = new_board
    return next_board, min_cost

def hc(n):
    board = initialize(n)
    moves = 0
    path = [board]
    costs = [calcCost(board)]
    for i in range(10000):
        cost = calcCost(board)
        if cost == 0:
            return path, moves, costs
        next_board, next_cost = move(board)
        if next_cost < cost:
            board = next_board
            path += [board]
            costs.append(next_cost)
            moves += 1
    return path, moves, costs

path, moves, costs = hc(8)
for i in path:
    for j in i:
        print(j)
    print()

print("Moves", moves)
print("Cost", costs)

plt.plot(range(len(costs)), costs)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost vs Iteration')
plt.show()
