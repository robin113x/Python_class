#!/bin/python3
from os import path, system as sy
sy('bash bash.sh')

fname=input('Enter file name : ')

res = path.isfile(fname)

if res:
    with open(fname,'r') as f:
        lno=cword=ccount=0
        for line in f:
            lno+=1
            cword+=len(line.split()) 
            ccount+=len(line)    
        print(lno)
        print(cword)
        print(ccount)
else:
    print("i'm sorry babu")
        

        

