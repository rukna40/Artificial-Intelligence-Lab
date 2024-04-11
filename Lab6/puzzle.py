def find(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(mat[i][j] == 0):
                return i,j

def genChild(mat):
    x,y=find(mat)
    val = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    children=[]
    for move in val:
        if 0<=move[0]<len(mat) and 0<=move[1]<len(mat):
            child = [row[:] for row in mat] 
            child[x][y],child[move[0]][move[1]]=child[move[0]][move[1]],child[x][y]
            children.append(child)
    return children

def calc(mat,goal):
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != goal[i][j]:
                count += 1
    return count

def hcp(start,goal,iters):
    curr=start
    path=[curr]
    count=0
    for i in range(iters):
        curr_cost=calc(curr,goal)
        if curr_cost==0:
            break
        costs=[]
        for child in genChild(curr):
            next_cost=calc(child,goal)
            costs.append((next_cost,child))
        costs.sort()    
        min=costs.pop(0)    
        if curr_cost>min[0]:  
            count+=1         
            path.append(min[1])
            curr=min[1]
    return path,count

start = [[1,2,3], [0,4,6], [7,5,8]]
end = [[1,2,3], [4,5,6], [7,8,0]]

path,cost=hcp(start,end,1000)
for i in path:
    for j in i:
        print(j)
    print()
print("Cost = ",cost)