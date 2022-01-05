#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

'''
compile()
finditer()
start()
end()
group()

'''
import re

pattern=re.compile('ab')

matcher=pattern.finditer('abaababaaabbab')
count=0
for match in matcher:
    count+=1
    print('Match is available at start index : ',match.start())

print("the no of occurrence : ",count)
