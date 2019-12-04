with open("input3") as f:
    wires  = f.readlines()
def getvisited(wire):
    x,y=0,0
    visited = {}
    dirX={'L':-1,'R':1,'U':0,'D':0}
    dirY={'L':0,'R':0,'U':1,'D':-1}
    distance = 0
    for i in wire.split(','):
        for j in range(int(i[1:])):
            x+=dirX[i[0]]
            y+=dirY[i[0]]
            #assume only go in one direction at once, given input structure
            distance+=1
            if (x,y) not in visited:
                visited[(x,y)]=distance
            print(len(visited),end='\r')
    print('\ndone')
    return visited
v1 = getvisited(wires[0])
v2 = getvisited(wires[1])
intersect = set(v1.keys()) & set(v2.keys())
print(min([abs(x)+abs(y) for (x,y) in intersect]))
print(min([v1[(x,y)]+v2[(x,y)] for (x,y) in intersect]))
