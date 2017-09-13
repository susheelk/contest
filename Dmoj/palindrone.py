import sys
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

while True:
    print fact(input()) % (2**32)
