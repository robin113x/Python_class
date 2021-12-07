#!/bin/python3

n = int(input('Enter the range of list : '))
l = [x for x in range(1,n+1)]
print(l)
print('Even no : ',end='')
l1 = list(filter(lambda n : n%2==0, l))
print(l1)
print('Odd no : ',end='')
l2 = list(filter(lambda n : n%2!=0, l))
print(l2)

print('odd and div by 3')

l3 = list(filter(lambda n : n%3==0 and n%2!=0,l))
print(l3)


print('Display Name Start with k')
names = ['Kat','kareena','kittu','kallu','bhallu','rosh','hood','robin','neha']
print(names)
l4 = list(filter(lambda name:name[0]=='k' or name[0]=='K',names))
print(l4)
