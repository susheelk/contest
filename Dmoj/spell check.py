inp = ""
toPrint = []
counter = 0
while inp !="No More Words!":
    counter +=1
    inp = raw_input()
    inpl = list(inp)
    
    if inp !="No More Words!":

        for i in range(len(inpl)-1):
            if (inpl[i]+inpl[i+1]) == "ie":
                if inpl[i-1] == "c":
                    inpl[i]="e"
                    inpl[i+1] = "i"
                    toPrint.append("".join(inpl))

            if (inpl[i]+inpl[i+1]) == "ei":
                if inpl[i-1] != "c":
                    inpl[i]="i"
                    inpl[i+1] = "e"
                    toPrint.append("".join(inpl))
            
        if "".join(inpl) == inp:
            toPrint.append("Word "+str(counter)+" is correct.")
            
               
for i in toPrint:
    print i
