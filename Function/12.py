#!/bin/python3
'''
map(function,sequence)

'''
n = int(input('Enter the range of list : '))

l = [ x for x in range(1,n+1)]
print(l)

def sqIt(n):
    return n*n
out = map(sqIt,l)
print(list(out))

print('Map with lambda function')

out = list(map(lambda n : n*n,l))
print(out)

