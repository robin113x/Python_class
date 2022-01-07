#!/bin/python3

n=int(input('Enter the no of Student : '))
d={}
for i in range(n):
    name=input('Enter the student name : ')
    marks=int(input('Enter the marks of student : '))
    d[name]=marks

print('\n\tStudent info ')
print('*'*30)

print(' Name \t\t Marks')
for k,v in d.items():
    print(k,'\t\t',v)

print('Search operation Start  :')

while True:
    name = input('Enter the Student Name : ' )
    marks = d.get(name,-1)
    if marks==-1:
        print("I'm sorry Babu : ")
    else:
        print(name,' Score : ',marks)
    opt=input('Do you want to continue Y/N : ')
    if opt=='N' or opt=='n':
        break

print('Thank you ')


