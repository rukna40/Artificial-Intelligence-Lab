
class graph():
    def __init__(self,n):
        self.adjlist={}
        self.v=n
        
    def addEdge(self,a,b,w):
        if a not in self.adjlist:
            self.adjlist[a]={b:w}
        else:
            self.adjlist[a][b]=w

    def aStar(self,start,end):
        q=[(0,start,[start])]
        while q:
            cur_cost,cur_node,path=q.pop(0)
            if cur_node==end:
                return cur_cost,path
            for neighbor in self.adjlist[cur_node]:
                if neighbor not in path:
                    q.append((cur_cost+self.adjlist[cur_node][neighbor],neighbor,path+[neighbor]))
                    q.sort()
                            
g=graph(12)

g.addEdge('A', 'B', 3)
g.addEdge('A', 'C', 2)
g.addEdge('B', 'A', 5)
g.addEdge('B', 'C', 2)
g.addEdge('B', 'D', 2)
g.addEdge('B', 'E', 3)
g.addEdge('C', 'A', 5)
g.addEdge('C', 'B', 3)
g.addEdge('C', 'F', 2)
g.addEdge('C', 'G', 4)
g.addEdge('D', 'H', 1)
g.addEdge('D', 'I', 99)
g.addEdge('F', 'J', 99)
g.addEdge('G', 'K', 99)
g.addEdge('G', 'L', 3)

cost,path=g.aStar('A','E')
print(path)
print(cost)
# print(g.adjlist)