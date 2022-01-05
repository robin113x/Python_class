#!/bin/python3

import re

matcher=re.finditer('ab','abcderfvefgb')
for m in matcher:
    print(m.start(),m.end(),m.end())

