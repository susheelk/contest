lst = [input(), input()]

i=1

while True:
    lst.append(lst[i-1] - lst[i])
    if(lst[i+1] > lst[i]):
        break
    i+=1

print len(lst)
