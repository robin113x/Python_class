

#!/bin/python3


'''
1.Empty Tuple  t=()
2.Single Valed Tuple t=10, //t=(10,)
3.MultiValed Tuple  t=(10,20,30,)
4.Tuple()Function  --->  t=tuple(seq.....)
5.Dynamic Input -----> eval(input(******))
'''
l1 = [1,2,3,4,5,6]
print(type(l1))
print(l1)
t1 = tuple(l1)
print(type(t1))
print(t1)


t2 = tuple(range(1,20,2))
print(type(t2))
print(t2)

t3 = eval(input('Enter the Tuple : '))
print(type(t3))
print(t3)




