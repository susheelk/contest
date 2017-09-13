lst = []
string = "BASNBAS"
level = 0
inds = []
for i in range(len(string)):
    if(string[i] == "B"):
        inds.append(i)
        level += 1
    if string[i] == "S":
        if (i == len(string)-1):
            level -= 1
            lst.append(string[inds.pop(inds[-1]):i + 1])
        elif(string[i+1] == "N"):
            level -= 1
            lst.append(string[inds.pop(inds[-1]):i+1])

