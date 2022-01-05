#!/bin/python3

import re
s=input('Enter pattern : ')
m=re.search(s,'abcdef')
if m!=None:
    print('search is found')
    print('Start {} End {} '.format(m.start(),m.end()))
else:
    print('404 not found')

