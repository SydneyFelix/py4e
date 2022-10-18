fhand = open('myhelp1.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for w in words :
        counts[w] = counts.get(w,0) + 1

for v,k in sorted(((v,k) for k,v in counts.items()),reverse=True)[:10]:print(k,v)
