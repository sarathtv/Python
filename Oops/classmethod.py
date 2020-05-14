#class methods and static methods

#attributes and methods


class Employee:
	#class variable
	raise_amount =1.04
	num_emps=0


	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.email=first+ '.'+last+ '@mail.com'
		self.pay=pay

		Employee.num_emps +=1  

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amount)
		#self.pay=int(self.pay*Employee.raise_amount)
		
		#turn regular method  as class method,, recieves class as arg instead of isntane
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount=amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split('-')
		return cls(first,last,pay)

#static methods  dont pass anything automatically ...
	@staticmethod
	def is_workday(day):
		if day.weekday()==5  or day.weekday()==6:
			return False
		return True	





emp_1 =Employee('sarath','tv',50000)
emp_2= Employee('test','testing',30000)

import datetime
my_date =datetime.date(2016,7,10)

print(Employee.is_workday(my_date))


#create instance from a string.
# emp_str_1 ='john-Doe-7000'

#first,last,pay=emp_str_1.split('-')
#new_emp=Employee(first,last,pay)
# print(new_emp.first)
## alternative
# new_emp=Employee.from_string(emp_str_1)
# print(new_emp.email)





#class method can be used from instance of class
# emp_1.set_raise_amt(1.07)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

