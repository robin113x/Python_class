from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai']
designations=['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']

def get_fake_name():
	name=choice(alphabets).upper()
	n=randint(2,9)
	for i in range(n):
		name=name+choice(alphabets)
	return name

def get_fake_eno():
	eno='e-'
	for i in range(4):
		eno=eno+choice(digits)
	return eno

def get_fake_salary():
	esal=uniform(10000,50000)
	return esal

def get_fake_city():
	city=choice(cities)
	return city

def get_fake_mno():
	mno=choice('6789')
	for i in range(9):
		mno=mno+choice(digits)
	return mno

def get_fake_designation():
	designation=choice(designations)
	return designation

def get_fake_emp_data():
	print('Employee Name:',get_fake_name())
	print('Employee Number:',get_fake_eno())
	print('Employee Salary:{:.2f}'.format(get_fake_salary()))
	print('Employee City:',get_fake_city())
	print('Employee Mobile Number:',get_fake_mno())
	print('Employee Designation:',get_fake_designation())

for i in range(10):
	get_fake_emp_data()
	print()
