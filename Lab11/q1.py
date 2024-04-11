import random

def initialize(n):
    board=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        board[i][random.randint(0,n-1)]=1

def calcCost(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                for k in range(i+1,len(board)):
                    if [k][j]==1:
                        cost+=1
                for k in range(j+1,len(board)):
                    if [i][k]==1:
                        cost+=1
                
