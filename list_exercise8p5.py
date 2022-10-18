fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
b = False
for l in fh:
    l.strip()
    l.rstrip()
    if l.startswith('From'):
        if b is True:
            b = False
            continue
        b = True
        l = l.split(' ')
        l = l[1]
        l = l.split(',')
        l = str(l)
        l = l[2:-2]
        print(l)

        count +=1

print("There were", count, "lines in the file with From as the first word")
