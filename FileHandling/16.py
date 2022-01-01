#!/bin/python3
from os import path, system as sy
sy('bash bash.sh')

import csv
i=0

with open('emp.csv','r') as f:
    r=csv.reader(f)
    data = list(r)
    print(data)

    for row in data:
        print(row)
    
    for row in data:
        for coloum in row:
           print(coloum ,'\t',end=" ")
        print(" ")
