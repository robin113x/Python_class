#!/bin/python3
supermarket = {
        'store1': {
                'name':'Robin Hood',
                'items':[
                    {'name':'soap','qnt':40},
                    {'name':'brush','qnt':80},
                    {'name':'tel','qnt':30},
                ]

            },
            'store2':{
                'name':'Neha kumari',
                'items':[
                    {'name':'java','qnt':40},
                    {'name':'c++','qnt':40},
                    {'name':'python','qnt':400},
                ]
            }
        }

print(supermarket['store1'])
print(supermarket['store1']['name'])
print(supermarket['store2']['name'])
print(supermarket['store1']['items'])

for d in supermarket['store1']['items']:
    print(d['name'])


for d in supermarket['store2']['items']:
    if d['name']=='python':
        print(d['qnt'])

