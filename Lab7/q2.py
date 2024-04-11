
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
            if cur_node in end:
                return cur_cost,path
            for neighbor in self.adjlist[cur_node]:
                if neighbor not in path:
                    q.append((cur_cost+self.adjlist[cur_node][neighbor]+self.heu[neighbor],neighbor,path+[neighbor]))
                    q.sort()
                            
g=graph(10)

g.adjlist = {
    'S': {'A':5, 'B':9, 'D':6},
    'A': {'S':5, 'G1':9, 'B':3},
    'B': {'A':2, 'C':1},
    'C': {'G2':5, 'S':6, 'F':7},
    'D': {'C':2, 'E':2, 'S':1},
    'E': {'G3':7},
    'F': {'D':2, 'G3':8},
    'G1': {},
    'G2': {},
    'G3': {}
}
g.heu = {
    'S':5,
    'A':7,
    'B':3,
    'C':4,
    'D':6,
    'E':5,
    'F':6,
    'G1':0,
    'G2':0,
    'G3':0
}

cost,path=g.aStar('S',['G1','G2','G3'])
print(path)
print(cost)
# print(g.adjlist)