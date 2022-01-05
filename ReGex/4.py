#!/bin/python3

import re
s=input('Enter pattern : ')
m=re.match(s,'abcdef')
if m!=None:
    print('it is found ')
    print('Start {} End {} '.format(m.start(),m.end()))
else:
    print('404 not found')

