#!/bin/python3
import json

employee={
        'name':'robin',
        'age':21,
        'salary':2000000,
        'isMarried':False,
        'GirlFriend':None
        }
json_string=json.dumps(employee)

print(json_string)
json_string=json.dumps(employee,indent=4)
print(json_string)

json_string=json.dumps(employee,indent=4,sort_keys=True )
print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=2,sort_keys=True)



