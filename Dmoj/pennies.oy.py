from math import pi
from math import ceil

p = None
lst = []

while p != 0:
    p = input()
    if p != 0:
        lst.append(int(ceil(pi*p*p+0.5)))

for i in lst: print i
