import sys
import os
sys.path.append(os.path.abspath("/home/ankur/Codes/ailab/Lab1&2"))
import graph

def solve(g,start):
    stack = [(start, [start])]
    path=[]
    while stack:
        node,path=stack.pop()
        if node==20:
            break
        for neighbor in g.adjList[node]:
            if neighbor not in path:
                    stack.append((neighbor,path+[neighbor]))     
    return path

if __name__=="__main__":
    n = 21
    g = graph.UGraph(n)

    g.adjList={
        1:[2,6],
        2:[1,3],
        3:[2,8],
        4:[5],
        5:[4,10],
        6:[1,11],
        7:[8],
        8:[3,7],
        9:[10,14],
        10:[5,9,15],
        11:[6,12],
        12:[11,17],
        13:[14],
        14:[13,9,19],
        15:[10,20],
        16:[17],
        17:[12,16,18],
        18:[17,19],
        19:[14,18],
        20:[15],
        0:[2,5]
    }

    print(solve(g,2))

    