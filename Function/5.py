#!/bin/python3

def f1(*n):
    print(n)

f1()
f1(1,2,3,4,5,6)




#---> Keyword Arguments **kwargs

def f2(**kwargs):
    print(kwargs)
    return

f2()
f2(name='Robin',dost='Neha')


#--------------------------------
def f3(*args,**kwargs):
    print(args)
    print(kwargs)
    return

f3()
f3(10,20,30,a=10,b=85)

