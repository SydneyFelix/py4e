#create an empty list and dictionary
counts = {}
lst = []

#opening a file in the same directory
Fh = open('myhelp1.txt')

#making a histogram

for line in Fh:
	line = line.rstrip()
	wds = line.split()
	for w in wds:
	 	counts[w] = counts.get(w, 0) + 1

#sorting descendingly and then getting the top 5 words:
lst = [(item[1],item[0]) for item in sorted([(v,k) for k, v in counts.items()],reverse=True)]

for item in lst[:5]:
    print(item)


# for item in lst:
# 	kv = (item[1],item[0])
# kv = kv[:5]
# print(kv)
