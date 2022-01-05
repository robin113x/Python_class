#!/bin/python3

import re
s=input('Enter pattern : ')
m=re.fullmatch(s,'abcdef')
if m!=None:
    print('full string matched ')
    print('Start {} End {} '.format(m.start(),m.end()))
else:
    print('404 not found')

