class DUGraph:
    def __init__(self,n):
        self.vertices=n
        self.adjList={}
        self.adjMat = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,a,b):
        self.adjMat[a][b]=1
        if a not in self.adjList:
            self.adjList[a]=[b]
        else:
            self.adjList[a].append(b)

class DWGraph:
    def __init__(self,n):
        self.vertices=n
        self.adjList={}
        self.adjMat = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,a,b,w):
        self.adjMat[a][b]=w
        if a not in self.adjList:
            self.adjList[a]=[(b,w)]
        else:
            self.adjList[a].append((b,w))

class UGraph:
    def __init__(self,n):
        self.vertices=n
        self.adjList={}
        self.adjMat = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,a,b):
        self.adjMat[a][b]=1
        self.adjMat[b][a]=1

        if a not in self.adjList:
            self.adjList[a]=[b]
        else:
            self.adjList[a].append(b)

        if b not in self.adjList:
            self.adjList[b]=[a]
        else:
            self.adjList[b].append(a)
            
class DWA1Graph:
    def __init__(self,n):
        self.vertices=n
        self.adjList={}
        self.adjMat = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,a,b,w):
        if a=='S':
            a=0
        elif a=='G':
            a=6
        if b=='S':
            b=0
        elif b=='G':
            b=6
        self.adjMat[a][b]=w
        if a not in self.adjList:
            self.adjList[a]=[(b,w)]
        else:
            self.adjList[a].append((b,w))

class DWAGraph:
    def __init__(self,n):
        self.vertices=n
        self.adjList={}
        self.nodes={}
        self.adjMat = [[0 for j in range(n)] for i in range(n)]


    def addNodes(self, nodes):
        count=0
        for node in nodes:
            self.nodes[node] = count
            count+=1

    def addEdge(self,a,b,w):
        self.adjMat[self.nodes[a]][self.nodes[b]]=w
        if a not in self.adjList:
            self.adjList[a]=[(b,w)]
        else:
            self.adjList[a].append((b,w))



if __name__=='__main__':
    n = 6 
    g = UGraph(n)

    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(3, 2)
    g.addEdge(4, 5)

    # g.addEdge(0, 1, 6)
    # g.addEdge(1, 2, 7)
    # g.addEdge(2, 0, 5)
    # g.addEdge(2, 1, 4)
    # g.addEdge(3, 2, 10)
    # g.addEdge(4, 5, 1)
    # g.addEdge(5, 4, 3)

    print("Adjacency List:")
    for vertex in g.adjList.items():
        for neighbor in vertex[1]:
            print("(",vertex[0],'->',neighbor,")",end=" ")
        print()
        

    print("\nAdjacency Matrix:")
    for row in g.adjMat:
        print(row)

