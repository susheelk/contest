initNo=input()

while True:
    noFactors=0
    initNo+=1
    rsqrt=initNo**(1.0/2)
    sqrt=int(rsqrt)
    if not (str(rsqrt).isdigit()):
        for i in range(2, sqrt+1):
            if initNo%i==0:
                    noFactors+=1
        if noFactors==0:
            break
    

print initNo
