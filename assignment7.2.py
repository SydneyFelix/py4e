import re
fname = input("Enter file name: ")
fh = open(fname)
c = 0
for line in fh:
    line.strip()
    if not line.startswith("X-DSPAM-Confidence:"):continue
    elif c==0:
        c += 1
        line.strip()
        new_x = re.findall('[0-9].+',line)
        new_x = float(new_x[0])
        ave = new_x
        old_x = new_x
    else:
        c += 1
        line.strip()
        new_x = re.findall('[0-9].+',line)
        new_x = float(new_x[0])

        temp_x = new_x
        new_x = new_x + old_x
        old_x = new_x
        ave = new_x / c
print('Average spam confidence:%s' % ave)
