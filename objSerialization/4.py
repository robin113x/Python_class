#!/bin/python3

import json

with open('emp.json','r')as f:
    emp=json.load(f)

for x,y in emp.items():
    print(x,':',y)

