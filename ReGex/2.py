#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

import re

pattern=re.compile('ab')

matcher=pattern.finditer('abababbaabab')  #matcher = re.finditer('ab','ababab')

count=0
for match in matcher:
    count+=1
    print('start :{},end:{},Group:{}'.format(match.start(),match.end(),match.group()))
print('No of occrrences : ',count)


