#!/bin/python3
from os import system as sy
sy('bash bash.sh')

with open('RobiNeha.txt','w') as f:
    f.write('Robin \n')
    f.write('Neha\n')
    f.write('Robin\n')
    f.write('Neha\n')
    print('Is File closed ',f.closed)
print('Is File closed ',f.closed)




