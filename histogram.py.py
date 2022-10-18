myf = input("Input a file name:")

hand = open(myf)
di = dict()
for lin in hand:
    if len(lin) > 1 :
        lin = lin.rstrip()

        wds = lin.split()

        for w in wds :
            # if w in di :
            #     di[w] = di[w] + 1
            # else:
            #     di[w] =  1
            di[w] = di.get(w, 0) + 1


print(di)

largest = -1
Swo_rd = ""
Lwo_rd = None
smallest = 1

for k,v in di.items():
    if v > largest :
        largest = v
        Lwo_rd = k
#In case there are multiple words that consist the largest. For instance
# if it turns out that the largest words are not just 'are' but also 'by' and 'with' and all has a count equals 100
    elif v == largest :
        Lwo_rd = Lwo_rd + "/" + k
    else:
        if v < smallest :
            Swo_rd = k
            smallest = v
#In case there are multiple words that consist the smallest. For instance
# if turns out that the smallest words are not just 'are' but also 'by' and 'with' and all has a count equals 1
        elif v == smallest:
            Swo_rd = Swo_rd + "/" + k
        else: continue





print("The most common word is %s = %d" % (Lwo_rd, largest))
print("Except those that are just one, the word containing the least count is %s = %d" % (Swo_rd, smallest))
