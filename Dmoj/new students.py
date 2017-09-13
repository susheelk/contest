marks = [float(input()) for x in range(input())]

t = input()
lst = []
for i in range(t):
    marks.append(input())
    lst.append(sum(marks)/len(marks))

for i in lst:
    m = round(i, 3)
    print '%.3f'%m
