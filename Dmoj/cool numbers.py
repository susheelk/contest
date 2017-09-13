
lst = [i**6 for i in range(25)]

a,b = input(), input()




inda = 0
indab = 0

for i in range(len(lst)):
    if lst[i] >= a:
        inda = i
        break

for i in range(len(lst)):   
    if lst[i] >= b:
        indb = i
        break

if inda == indb:
    if a in lst:
        print 1
    else:
        print 0
else:
    lst2 = lst[inda:indb]
            

    print len(lst2)

#99, 379
