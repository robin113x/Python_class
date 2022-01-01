#!/bin/python3
from os import path, system as sy1
sy('bash bash.sh')

import csv
i=0
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['ID','NAME','Salary'])
    while True:
        idno = int(input("Enter ur id : "))
        name = input('Enter ur name : ')
        sal = float(input('Enter salary : '))
        w.writerow([idno,name,sal])
        i+=1
        if i==3:
            break