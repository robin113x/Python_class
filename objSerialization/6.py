#!/bin/python3
from pyaml import yaml

emp_dict={
    'name':'Robin',
    'age':21,
    'salary':200001000.0,
    'isMarried':True
    }

#Serialization
y_string=yaml.dump(emp_dict)

print(y_string)

#Serialization to yaml file
with open('emp.yaml','w') as f:
    yaml.dump(emp_dict,f)

#Deserialization
ed=yaml.safe_load(y_string)
print(ed)


with open('emp.yaml','r') as f:
    edf=yaml.safe_load(f)
print(edf)