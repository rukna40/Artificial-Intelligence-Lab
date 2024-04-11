
class graph():
    def __init__(self,n):
        self.adjlist={}
        self.v=n
        self.heu={}
    def addEdge(self,a,b,w):
        if a not in self.adjlist:
            self.adjlist[a]={b:w}
        else:
            self.adjlist[a][b]=w

    def aStar(self,start,end):
        q=[(self.heu[start],start,[start])]
        while q:
            cur_cost,cur_node,path=q.pop(0)
            if cur_node==end:
                return cur_cost,path
            for neighbor in self.adjlist[cur_node]:
                if neighbor not in path:
                    q.append((cur_cost+self.adjlist[cur_node][neighbor]+self.heu[neighbor],neighbor,path+[neighbor]))
                    q.sort()
                            
g=graph(10)

g.addEdge('A', 'B', 6)
g.addEdge('A', 'F', 3)
g.addEdge('B', 'A', 6)
g.addEdge('B', 'C', 3)
g.addEdge('B', 'D', 2)
g.addEdge('C', 'E', 5)
g.addEdge('C', 'D', 1)
g.addEdge('C', 'B', 3)
g.addEdge('D', 'B', 2)
g.addEdge('D', 'C', 1)
g.addEdge('D', 'E', 8)
g.addEdge('E', 'C', 5)
g.addEdge('E', 'D', 8)
g.addEdge('E', 'I', 5)
g.addEdge('E', 'J', 5)
g.addEdge('F', 'A', 3)
g.addEdge('F', 'G', 1)
g.addEdge('F', 'H', 7)
g.addEdge('G', 'F', 1)
g.addEdge('G', 'I', 3)
g.addEdge('H', 'F', 7)
g.addEdge('H', 'I', 2)
g.addEdge('I', 'E', 5)
g.addEdge('I', 'G', 3)
g.addEdge('I', 'H', 2)
g.addEdge('I', 'J', 3)
g.addEdge('J', 'E', 5)
g.addEdge('J', 'I', 3)

g.heu = {
    'A':10,
    'B':8,
    'C':5,
    'D':7,
    'E':3,
    'F':6,
    'G':5,
    'H':3,
    'I':1,
    'J':0
}

cost,path=g.aStar('A','J')
print(path)
print(cost)
# print(g.adjlist)