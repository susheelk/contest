lst = []
dic = {True: "Yes", False: "No"}
for i in range(input()):
    w = [raw_input(), raw_input(), raw_input()]
    prefixFree = True
    for i in w:
        l = [z for z in w if z != i]
        for b in l:
            if b in i:
                if i.index(b) == 0:
                    prefixFree = False
                    break
    
    suffixFree = True
    for i in w:
        l = [z for z in w if z != i]
        for b in l:
            if b in i:
                if i.index(b) == len(i)-len(b):
                    suffixFree = False
                    break

    lst.append(dic[suffixFree and prefixFree])

for i in lst:
    print i

        
