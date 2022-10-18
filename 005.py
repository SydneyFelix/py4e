book = open('checklist.txt')
count = 0
for eachline in book :
    count = 0 + 1
    eachline = eachline.rstrip()
    if eachline.startswith('how'):
        print(eachline)

print('total lines:', count)
