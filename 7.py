# fhandler = ""
try:
    fhandler = open('myelp.txt')
except:
    print("Invalid filename.")
    quit()



counter = fhandler.read()
print(len(counter))
# print(counter[:1404])
