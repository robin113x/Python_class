class Car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def getinfo(self):
		print('\tCar Name:{}\n\tModel:{}\n\tColor:{}'.format(self.name,self.model,self.color))
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eatndrink(self):
		print('Eating Biryani and Drinking Beer')
class Employee(Person):
	def __init__(self,name,age,eno,esal,car):
		super().__init__(name,age)
		self.eno=eno
		self.esal=esal
		self.car=car
	def work(self):
		print('Coding Python Programs..')
	def empinfo(self):
		print('Employee Name:',self.name)
		print('Employee Age:',self.age)
		print('Employee Number:',self.eno)
		print('Employee Salary:',self.esal)
		print('Employee Car Information:')
		self.car.getinfo() # Employee using Car Functionality

car=Car('Innova','2.5V','Grey')
e=Employee('Durga',48,872425,10000,car)
e.eatndrink() #Employee using Person class functionality
e.work()
e.empinfo()