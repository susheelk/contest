string = raw_input()

c = string.index("C")
d = string.index("D")
h = string.index("H")
s = string.index("S")


lst = [ list(string[c+1:d]),
        list(string[d+1:h]),
        list(string[h+1:s]),
        list(string[s+1:]) ]

pts = [4*i.count("A")+3*i.count("K")+2*i.count("Q")+i.count("J") for i in lst]

##for i in range(len(lst)):
##    dbls = []
##    singles = []
##    for x in lst[i]:
##        if lst[i].count(x) == 2:
##            dbls.append(x)
##        if lst[i].count(x) == 1:
##            singles.append(x)
##            
##
##    dbls = set(dbls)
##    singles = set(singles)
##
##    pts[i]+= 2*len(singles)+len(dbls)
##

lens = map(len, lst)

for i in range(len(lens)):
    if lens[i] == 0:
        pts[i]+=3
    if lens[i] == 1:
        pts[i]+=2
    if lens[i] == 2:
        pts[i]+=1


for i in range(len(lst)):
    st = str(lst[i]).replace(",", " ")
    st = st.replace("[", "")
    st = st.replace("]", "")
    st = st.replace("'", "")
    lst[i] = st

pts = map(str, pts)

print("Cards Dealt  Points")
print("Clubs "+lst[0]+" "+pts[0])
print("Diamonds "+lst[1]+" "+pts[0])
print("Hearts "+lst[2]+" "+pts[0])
print("Spades "+lst[3]+" "+pts[0])
pts = map(int, pts)
print("Total "+str(sum(pts)))

