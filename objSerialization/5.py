#!/bin/python3
import jsonpickle
class Employee:
	def __init__(self,eno,ename,esal,eaddr,isMarried):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
		self.isMarried=isMarried

	def display(self):
		print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}, IsMarried{}'.format(self.eno,self.ename,self.esal,self.eaddr,self.isMarried))

 #Serialization to String
e=Employee(100,'Durga',1000.0,'Hyderabad',True)
json_string = jsonpickle.encode(e)
print(json_string)

#Serialization to file
with open('emp.json','w') as f:
    f.write(json_string)

#Deserialization
newEmp=jsonpickle.decode(json_string)
newEmp.display()

#Deserialization From the file
with open('emp.json','r') as f:
    json_string=f.readline()
newEmp=jsonpickle.decode(json_string)
newEmp.display()
