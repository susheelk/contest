lst = []

for i in range(input()):
    input()
    words = raw_input().split(" ")
    for x in range(len(words)):
        words[x] = words[x].replace(".", "!!!")
        if(words[x].upper() == words[x] and not (words[x].isdigit()) and any(c.isalpha() for c in words[x] )):
            words[x] = "!!!"+words[x]+"!!!"

    lst.append(" ".join(words))

for i in lst:
    print i
        
