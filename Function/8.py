#!/bin/python3

sum = lambda a,b:a+b

res = sum(10,20)
print(res)


out = lambda a,b:a if a>b else b
print(out(10,96))


bigger = lambda a,b,c : a if a>b and a>c else b if b>c else c
print(bigger(10,20,90))


