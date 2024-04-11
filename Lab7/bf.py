
class graph():
    def __init__(self,n):
        self.adjMat=[[0 for i in range(n)] for j in range(n)]
        self.v=n
        self.heu={}
    def addEdge(self,a,b,w):
        self.adjMat[ord(a)-65][ord(b)-65]=w

    def bf(self,start):
        dist={}
        prev={}
        for i in range(len(self.adjMat)):
            dist[i]=float('inf')
            prev[i]=None
        dist[ord(start)-65]=0   
        for _ in range(len(self.adjMat)-1):
            for v in range(len(self.adjMat)):
                for u in range(len(self.adjMat)):
                    if self.adjMat[u][v] != 0 and dist[u]+self.adjMat[u][v]<dist[v]:
                        dist[v]=dist[u]+self.adjMat[u][v]
                        prev[v]=u
        for u in range(len(self.adjMat)):
            for v in range(len(self.adjMat)):
                if self.adjMat[u][v] != 0 and dist[u]+self.adjMat[u][v]<dist[v]:
                    return None,None
        return dist,prev


        
        

                            
g=graph(5)

g.addEdge('A', 'B', 4)
g.addEdge('A', 'C', 2)
g.addEdge('B', 'C', 3)
g.addEdge('B', 'D', 2)
g.addEdge('B', 'E', 4)
g.addEdge('C', 'B', 1)
g.addEdge('C', 'D', 4)
g.addEdge('C', 'E', 5)
g.addEdge('E', 'D', -5)

dist,prev=g.bf('A')
print(dist)
print(prev)