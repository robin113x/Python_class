#!/bin/python3
'''
single valued tuple , t=(10,)

'''
t = (10,20,30,40)
print(type(t))

t1 = (10,40)
print(type(t1))

t2 = (10)         #this is not tuple , simple int type value
print(type(t2))




t3 = (10,)
print(type(t3))

t=()
print(type(t))
t=(10)
print(type(t))
t=10
print(type(t))
t=(10,)
print(type(t))
t=10,
print(type(t))
t=(10,20,30)
print(type(t))
t=(10,20,30,)
print(type(t))
t=10,20,30,
print(type(t))
t=10,20,30
print(type(t))

