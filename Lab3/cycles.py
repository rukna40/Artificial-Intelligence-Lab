import sys
import os
sys.path.append(os.path.abspath("/home/ankur/Codes/ailab/Lab1&2"))
import graph

def cycles(g,start):
    stack=[start]
    visited=[]
    flag=0

    while stack:
        node=stack.pop()
        visited.append(node)
        for neighbor in g.adjList[node]:
            if neighbor not in visited:
                    stack.append(neighbor)     
            else:
                flag=1  
    if flag==1:
        print("Cycle exists")
    else:
        print("Cycle does not exist ")

if __name__=="__main__":
    n = 4
    g = graph.DUGraph(n)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    cycles(g,2)

    