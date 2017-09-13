raw = raw_input()
rawL = []

dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


for i in range(0, len(raw), 2):
    rawL.append(raw[i]+raw[i+1])

fac = []

for i in range(0, len(rawL)-1):
    if dic[ rawL[i][1] ] >= dic[rawL[(i+1)][1]]:
        fac.append(1)
    else:
        fac.append(-1)
fac.append(1)
    
rawL2 = [(int(rawL[i][0])*dic[rawL[i][1]])*fac[i] for i in range(len(rawL))]

print sum(rawL2)
