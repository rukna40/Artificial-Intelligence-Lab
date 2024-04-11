
def find(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==' ':
                return i,j

def calcCost(mat, ans):
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != ans[i][j]:
                count += 1
    return count

def genChildren(mat):
    x,y=find(mat)
    steps=[(x,y+1),(x+1,y),(x,y-1),(x-1,y)]
    children=[]
    for step in steps:
        if 0<=step[0]<len(mat) and 0<=step[1]<len(mat[0]):
            temp=[row[:] for row in mat]
            temp[step[0]][step[1]], temp[x][y] = temp[x][y], temp[step[0]][step[1]]
            children.append(temp)
    return children


def aStar(start,end):
    q=[(calcCost(start,end),start,[start],0)]
    while q:
        cur_cost,cur_node,path,num=q.pop(0)
        if cur_node==end:
            return path,cur_cost,num
        children=genChildren(cur_node)
        for child in children:
            if child not in path:
                q.append((cur_cost+calcCost(child,end),child,path+[child],num+1))
                q.sort(key = lambda x: x[0])

start=[[2,8,3],[1,6,4],[7,' ',5]]
end=[[1,2,3],[8,' ',4],[7,6,5]]

path,cost,num=aStar(start,end)
for mat in path:
    for i in mat:
        print(i)
    print()
print(cost)