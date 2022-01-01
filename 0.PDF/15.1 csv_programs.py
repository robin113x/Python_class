Writing data to csv files:
-------------------------
import csv
with open('emp.csv','w',newline='') as f:
	w=csv.writer(f) #returns writer object to write data
	#print(type(w)) #<class '_csv.writer'>
	w.writerow(['ENO','ENAME','ESAL','EADDR'])
	while True:
		eno=int(input('Enter Employee Number:'))
		ename=input('Enter Employee Name:')
		esal=float(input('Enter Employee Salary:'))
		eaddr=input('Enter Employee Address:')
		w.writerow([eno,ename,esal,eaddr])
		option=input('Do You want to insert one more record [Yes|No]:')
		if option.lower()=='no':
			break
print('Total Employees data written to csv file successfully')

Reading data from csv files:
----------------------------
import csv
with open('emp.csv','r') as f:
	r=csv.reader(f) #returns csv reader object
	#print(type(r)) #<class '_csv.reader'>
	data=list(r)
	#print(data)
	for row in data:
		for column in row:
			print(column,'\t',end='')
		print()
