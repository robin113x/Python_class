#!/bin/python3

import json

json_string=''' {
    "name": "robin",
    "age": 21,
    "salary": 2000000,
    "isMarried": false,
    "GirlFriend": null

} '''

employee=json.loads(json_string)
print(type(employee))

for x,y in employee.items():
    print(x,'  : ',y)

