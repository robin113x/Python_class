#!/bin/python3
'''
filter(function, sequence)

'''
def isEven(n):
    if n%2==0:
        return True
    else:
        return False

n = eval(input('Enter the range of list : '))
l=[x for x in range(1,n+1)]
print(l)
l1=[]
for i in l:
    if isEven(i)==True:
        l1.append(i)
print(l1)

#with filter function

def isEven(n):
    if n%2==0:
        return True
    else:
        return False

n = int(input('Enter the Range of list : '))
l = [x for x in range(1,n+1)]
print(l)

l1 = filter(isEven,l)
print(list(l1))

print('filter with lambda function')

n = int(input('Enter the Range of list : '))
l = [x for x in range(1,n+1)]
print(l)
l1 = list(filter(lambda n:n%2==0,l))
print(l1)
