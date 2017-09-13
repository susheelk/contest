import sys
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


for i in range(input()):
    b = input()
    if b > 34:
        print 0
    else:
        print fact(b) % (2**32)
