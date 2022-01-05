#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

import re

l=re.split('-','10j-20-30-40-50')
print(l)


l2=re.split('[.]','www.RobinRoy.ml')
print(l2)

'''
. -> everything
[.] -> dot or \.


'''
