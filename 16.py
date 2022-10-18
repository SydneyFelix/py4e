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
smallest = 11

sw=None
lw=None

for k,v in di.items():
    # print("%s = %d "%(k,v))
    if v < smallest:
        smallest = v
        sw = k
    elif v > largest:
            largest = v
            lw = k

    print("key =%s Value = %d  smallest = %s = %d  largest = %s = %d" % (k,v,sw,smallest,lw,largest))


print("Done! the least common word is '%s' with %d count" % (sw,smallest))




print("Done! the most common word is '%s' with %d counts" % (lw,largest))
