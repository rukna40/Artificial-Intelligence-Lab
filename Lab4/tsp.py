def tsp(g,start):
    queue=[(start,[start],0)]
    min_path=[]
    min_cost=float('inf')
    while queue:
        node,path,total_cost=queue.pop(0)
        if len(path)==len(g):
            if min_cost>total_cost:
                min_cost=total_cost
                min_path=path
        else:
            for neighbor, cost in graph[node].items():
                if neighbor not in path:
                    queue.append((neighbor,path+[neighbor],total_cost+cost))

    return min_path,min_cost
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}
start_node = 'A'

path, cost = tsp(graph, start_node)


print(path)
print(cost)