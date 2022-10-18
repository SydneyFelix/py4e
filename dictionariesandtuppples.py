#open the program
hfile = open('philokalia.txt',encoding='utf-8')
#modify the program so that in the end you have a histogram

#you are making an empty dictionary
di = dict()

#making a histogram
for line in hfile:
        line = line.rstrip()
        wds = line.split()
        for w in wds:
            di[w] = di.get(w,0) + 1  # ito yung nakakalito/hindi ako sigurddo
#get the top 5 words
myli = list()
for k,v in di.items():
    tup = (v,k)
    myli.append(tup)

myli = sorted(myli, reverse=True)
#
print((k,v) for v,k in myli[:5])
# for v,k in myli[:5]:
#      print(k,v)
