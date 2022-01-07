#!/bin/python3
n = int(input('Enter the no of Student  : '))
d={}
for i in range(n):
    name=input('Enter Name of Student : ')
    marks=int(input('Enter Marks of Student : '))
    d[name]=marks

print('*'*30)
print('Name ' ,'\t\t' ,'Marks')
for name in d:
    print(name,'\t\t',d[name])

print('*'*30)
