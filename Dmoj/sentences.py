toprint = []

for x in range(input()):
    nsub = input()
    bverb = input()
    nobj = input()
    
    subjects = [raw_input() for i in range(nsub)]
    verbs = [raw_input() for i in range(bverb)]
    objects = [raw_input() for i in range(nobj)]

    for s in subjects:
        for v in verbs:
            for o in objects:
                toprint.append(s+" "+v+" "+o+".")
for i in toprint:
    print i
