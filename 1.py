
f = open('myhelp2.txt')
D = {}
for l in f:
    l = l.strip()
    W = l.split()
    c=0
    for w in W:
        if w.startswith('CA'):
            D = D.get(w, 0) + 1
            c+=1
            print('True')
            continue
print('***********')
print(f'total= {list(D)}')
print('***********')
for key, value in D.items():
    k = key.ljust(15,'>')
    print(k,value)

print('total'.ljust(15,'>'),c)
