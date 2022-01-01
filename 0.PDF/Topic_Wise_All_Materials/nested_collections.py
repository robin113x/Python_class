market={
        'store1':{
            'name':'Durga Store',
            'items':[
                        {'name':'soap','quantity':20},
                        {'name':'brush','quantity':30},
                        {'name':'pen','quantity':40},
                    ]
            },
            'store2':{
                'name':'Sunny Store',
                'items':[
                            {'name':'python','quantity':100},
                            {'name':'java','quantity':200},
                            {'name':'django','quantity':300},
                        ]
                }
    }
#To display name of the first store
print(market.get('store1').get('name'))
print(market['store1']['name'])
#To display names of all items present inside store1
items = market['store1']['items']
for x in items:
	print(x['name'])
#To display quantity of item:'django' present in store2
items  = market['store2']['items']
for x in items:
	if x['name']=='django':
		print(x['quantity'])
