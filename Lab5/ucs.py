import sys
import os
sys.path.append(os.path.abspath("/home/ankur/Codes/ailab/Lab1&2"))
import graph

def ucs(g,start,end):
    if start=='S':
        start=0
    if end=='G':
        end=6
    queue=[(start,[start],0)]
    min_path=[]
    min_cost=float('inf')
    while queue:
        node,path,total_cost=queue.pop(0)
        if node==end:
            if min_cost>total_cost:
                min_cost=total_cost
                min_path=path
        for neighbor, cost in g.adjList[node]:
            if neighbor not in path and g.adjMat[node][neighbor]!=0:
                queue.append((neighbor,path+[neighbor],total_cost+cost))
                queue.sort(key=lambda a: a[2])


    return min_path,min_cost

if __name__=="__main__":
    n = 7
    g = graph.DWA1Graph(n)

    g.addEdge('S', 1, 2)
    g.addEdge('S', 3, 5)
    g.addEdge(3, 1, 5)
    g.addEdge(3, 'G', 6)
    g.addEdge(1, 'G', 1)
    g.addEdge(3, 4, 2)
    g.addEdge('G', 4, 7)
    g.addEdge(4, 5, 3)
    g.addEdge(4, 2, 4)
    g.addEdge(5, 'G', 3)
    g.addEdge(2, 1, 4)
    g.addEdge(5, 2, 6)


    path,cost=ucs(g,'S','G')
    print(path)
    print(cost)