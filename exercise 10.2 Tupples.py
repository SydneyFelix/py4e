#exercise 10.2 Tupples
import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
D = dict()
L = []
firstimer = True
for h in handle:
    if h.startswith('From'):
        h = h.strip()
        l = len(h)
        h = h[-13:-11]
        if h.isdigit(): L.append(int(h))

for l in L:
     D[l] = D.get(l,0)+1

D = sorted(D.items())

for d in D:
    a = d[0]
    b = d[1]


    if d[0] < 10:
        a = '0' + str(d[0])

    print(a,b)
