from sys import stdin

res = []

for x in range(int(stdin.readline())):
    maxv = int(stdin.readline())
    data = []
    for i in range(maxv):
        data.append(int(stdin.readline()))
    
    if (reversed(data) == sorted(data)):
        res.append("Y")
        continue

    needed = range(1, maxv+1)
    branch = []
    lake = []
    i = 1
    while (len(lake) != maxv) or (len(data)==0):
        if len(branch) != 0 and (branch[0] == i):
            lake = [branch.pop(branch.index(branch[0]))] + lake
            i+=1
        elif len(data) == 0:
            break
        elif data[-1] == i:
            lake = [data.pop(data.index(data[-1]))]+lake
            i+=1
        else:
            branch = [data.pop(data.index(data[-1]))] + branch

    if list(reversed(lake)) == sorted(list(reversed(lake))) and len(lake) == maxv:
        res.append('Y')
    else:
        res.append('N')

for b in res:
    print b

        
##        if i == 1:
##            current = data.pop(data[-1])
##            if current == i:
##                lake = [i]+lake
##            else:
##                branch = [i]+branch
##            
##        else:
            
                
