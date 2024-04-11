import sys
import os
sys.path.append(os.path.abspath("/home/ankur/Codes/ailab/Lab1&2"))
import graph

def ucs(g, start, end):
    queue = [(0, start, [start])]
    min_path = []
    min_cost = float('inf')

    while queue:
        queue.sort(key=lambda x: x[0])
        total_cost, node, path = queue.pop(0)
        if node in end:
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path

        if node in g.adjList:
            for neighbor, cost in g.adjList[node]:
                if neighbor not in path and g.adjMat[g.nodes[node]][g.nodes[neighbor]] != 0:
                    queue.append((cost + total_cost, neighbor, path + [neighbor]))

    return min_path, min_cost

if __name__ == '__main__':
    n = 10
    g = graph.DWAGraph(n)
    g.addNodes(['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G1', 'G2', 'G3'])
    g.addEdge('S', 'A', 5)
    g.addEdge('S', 'B', 9)
    g.addEdge('C', 'S', 6)
    g.addEdge('S', 'D', 6)
    g.addEdge('A', 'B', 3)
    g.addEdge('B', 'A', 3)
    g.addEdge('B', 'C', 1)
    g.addEdge('D', 'C', 2)  
    g.addEdge('D', 'E', 2)
    g.addEdge('E', 'G3', 7)
    g.addEdge('F', 'G3', 8)
    g.addEdge('F', 'D', 2)
    g.addEdge('C', 'F', 7)
    g.addEdge('C', 'G2', 5)
    g.addEdge('A', 'G1', 9)

    path, cost = ucs(g, 'S', ['G1', 'G2', 'G3'])
    print(path)
    print(cost)
