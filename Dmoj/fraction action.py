def simplify(num, denom):
    numFacs = []
    denomFacs = []
    common = []
    for i in range(1, num+1):
        if num % i == 0:
            numFacs.append(i)
    for i in range(1, denom+1):
        if denom % i == 0:
            denomFacs.append(i)
    for i in numFacs:
        if i in denomFacs:
            common.append(i)
    fac = max(common)
    l= [(num/fac), (denom/fac)]
    return str(l[0])+"/"+str(l[1])

num = input()
denom = input()

if num < denom and num != 0:
    print simplify(num, denom)

else:
    whole = num / denom
    num = num % denom
    if num == 0:
        print whole
    else:
        print str(whole) + " "+simplify(num, denom)


