def fib(s,e):
    a,b = s,e
    while True:
        yield a
        a, b = b, a + b

import types
start = int(input('input start number: '))
end = int(input('upto what number: '))
if type(fib(start,end))==types.GeneratorType: # this is optional
    print(type(fib(start,end)))# this is optional
    print("Good, you'r on the right track.")# this is optional
c = 0
for n in fib(start,end):
    # print(fib())
    print(n)
    c+=1
    if c == end:break
