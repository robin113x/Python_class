#!/bin/python3

import re

pat='asdf74wr1feg4rhbt45yrhntj4ntj5hmmgjhfdbvsf'
print(pat)
s=re.subn('[a-z]','#',pat)
print(s)
print(s[0])
print(s[1])

