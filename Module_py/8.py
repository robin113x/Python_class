#!/bin/python3
'''
Random Module
random()--- print random value b/w (0--1) /// >>>float
uniform(start,end) --- start < x < end ///>>>float
randint(start,end) ----  start<=x<=end ///>>int
randrange(start,end,step) --- from start to end-1 , start is optional ,
 default value is zero(0) , step =1(default) , end is mandatory 
randrange(5) ---- 0 to 4 [any random value]
choice(sequence) -----> may be list or tuple or string but not set or dict
'''
from random import *
for i in range(1,11):
    print(random())
    print(uniform(1,9))
    print(randint(1,7))
    print(randrange(5))
    print(randrange(0,11,2)) #---> odd value only
    print(randrange(0,101,10)) # 10,20,30,40,50,60,70,80,90,100

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(choice(alphabets))

