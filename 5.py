#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#	, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#	er of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
#	 the person who sent the mail. The program creates a Python dictionary that maps the sender's mail a
#	ddress to a count of the number of times they appear in the file. After the dictionary is produced,
#	the program reads through the dictionary using a maximum loop to find the most prolific committer.
import re
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
D = dict()
T = tuple()
L = list()
firstimer = True
for h in handle:
    h=h.strip()
    if h.startswith('From') and h[-1]=='8':
        h = h.split(' ')
        h = h[1]
        T = str(re.findall('\S+@\S+',h))
        T = str(T[1:-1])
        T = T[1:-1]
        D[T] = D.get(T,0)+1

D = sorted()
#
for k,v in v,k sorted(L,reverse=True)[:1]:
#     k = str(k[1:-1])
#     print(k,v)
#         VK=(D[T], K)
#         KV=(K,D[T])
#         L.append(VK)
#         # print(T)
# for v,k in sorted(L,reverse=True)[:1]:
#     k = str(k[1:-1])
#     print(k,v)
# # #
