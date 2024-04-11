import sys
import os
sys.path.append(os.path.abspath("/home/ankur/Codes/ailab/Lab1&2"))
import graph

def indegree(g):
    indeg=[0 for i in range(g.vertices)]
    for i in range(g.vertices):
        for j in range(g.vertices):
            if g.adjMat[j][i]==1:
                indeg[i]+=1
    return indeg


def topSortBFS(g):
    queue=[]
    visited=[]
    indeg=indegree(g)
    for i in range(g.vertices):
        if indeg[i]==0:
            queue.append(i)
            visited.append(i)
    while queue:
        print(queue)
        node=queue.pop(0)
        visited.append(node)
        # print(node)
        if node in g.adjList:
            for neighbor in g.adjList[node]:
                if neighbor not in visited:
                    indeg[neighbor]-=1
                    if indeg[neighbor]==0:
                        queue.append(neighbor)         

if __name__=="__main__":
    n = 6 
    g = graph.DUGraph(n)

    g.addEdge(5, 0)
    g.addEdge(5, 2)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    topSortBFS(g)

    