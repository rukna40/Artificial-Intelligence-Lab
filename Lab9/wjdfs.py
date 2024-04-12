def transition(j1,j2,w):
    stack=[(0,0,[],[])]
    visited=[]
    while stack:
        juga,jugb,path,actions=stack.pop()
        if juga==w or jugb==w:
            return True,path,actions
        if (juga,jugb) not in visited:
            visited.append((juga,jugb))

            if juga<j1:
                stack.append((j1,jugb,path+[(j1,jugb)],actions+["Filled jug 1"]))

            if jugb<j2:
                stack.append((juga,j2,path+[(juga,j2)],actions+["Filled jug 2"]))

            if juga>0:
                stack.append((0,jugb,path+[(0,jugb)],actions+["Emptied jug 1"]))

            if jugb>0:
                stack.append((juga,0,path+[(juga,0)],actions+["Emptied jug 2"]))

            if (juga+jugb)<=j1:
                stack.append((juga+jugb,0,path+[(juga+jugb,0)],actions+["Poured water from jug 2 to jug 1"]))
            else:
                stack.append((j1,juga+jugb-j1,path+[(j1,juga+jugb-j1)],actions+["Poured water from jug 2 to jug 1"]))
            
            if (juga+jugb)<=j2:
                stack.append((0,juga+jugb,path+[(0,juga+jugb)],actions+["Poured water from jug 1 to jug 2"]))
            else:
                stack.append((juga+jugb-j2,j2,path+[(juga+jugb-j2,j2)],actions+["Poured water from jug 1 to jug 2"]))

    return False,[],[]

j1=4
j2=3
w=2

found=transition(j1,j2,w)
if not found[0]:
    print("Not Possible")
else:
    for i in range(len(found[1])):
        print(found[1][i],found[2][i])
