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
		


print(Employee.num_emps)
emp_1 =Employee('sarath','tv',50000)
emp_2= Employee('test','testing',30000)


print(Employee.num_emps)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)

# #print(emp_1.__dict__)
# #print(Employee.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# Employee.raise_amount=1.05

# #emp_1.raise_amount=1.06
# print(emp_1.raise_amount)

# print(emp_2.raise_amount)