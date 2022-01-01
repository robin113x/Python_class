#!/bin/python3
from os import system  
system('bash bash.sh')

try:
    print('outer try block')
    print(10/0)
    try:
        print('inner try block')
        print(110/0)

    except ValueError as e:
        print('inner Error : ',e)

    finally:
        print('Inner finaally block')

except Exception as e:
    print(' outer error : ',e)
    
finally: 
    print('Outer finaally block')
    
