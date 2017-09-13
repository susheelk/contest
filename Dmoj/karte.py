inp = raw_input()
ans = (str(13-inp.count("P"))+" "+str(13-inp.count("K"))+" "+str(13-inp.count("H"))+" "+str(13-inp.count("T")))

lst = []

for i in range(0, len(inp), 3):
    lst.append(inp[i:i+3])

if len(set(lst)) == len(lst):
    print ans
else:
    print "GRESKA"
    
