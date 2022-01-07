#!/bin/python3
'''
set
'''
s={}    #bydefault it is Dict not set
print(type(s))
s=set()
s.add(10)
s.add(2)
s.add(23)
s.add(10)
print(s)

#creating set object's
'''
1.Empty set 
        s=set()
2.MultiValed set
        s={10,20,30,40,50,'A'}
3.By using set function
        l=[10,20,30,40,50]
        s=set(l)

4.      s=set('apple')
        print(s) ---> {a,p,l,e}
5.Dynamic input
    
    s=eval(input('Enter the set : '))
'''
s = set()
s=set('apple')
print(s)
s=eval(input('Enter the set : '))
print(type(s))
print(s)

#Mathemtical,Equality,Realtional and Membership Operators





