#!/bin/python3

def fab_gen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

g=fab_gen()
for x in g:
    print(x)