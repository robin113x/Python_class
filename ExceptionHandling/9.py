#!/bin/python3
from os import system as sy
sy('bash bash.sh')
f=None
try:
    f=open('bash.sh','r')
    
except Exception as e:
    print(e)
    print('Exception block')

else:
    print('file open successfully')
    print('*'*20)
    print(f.read())


finally:
    print('clean up code')
    if f is not None:
        f.close()
    

