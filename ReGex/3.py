#!/bin/python3

from os import system as sy
sy('clear')
sy('date')

import re

matcher = re.finditer('[^a-z]','abcx@k9dfs')

for m in matcher:
    print(m.start(),' ..... ',m.group())

