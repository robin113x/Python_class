#!/bin/python3

'''
Nested list as Matrix
'''

l=[[1,2,3,4],[5,6,7,8],[9,1,8,2]]
print(l)
print('Matrix')

for x in l:
    for y in x:
        print(y,end=' ')
    print()
