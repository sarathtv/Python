## magic methods
class Employee:
	#class variable
	raise_amount =1.04
	

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.email=first+ '.'+last+ '@mail.com'
		self.pay=pay

	
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amount)
	
	def __repr__(self):
		return"Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

	def __str__(self):
		return"{}-{}".format(self.fullname(),self.email)

	def __add__(self,other):
		return self.pay+other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 =Employee('sarath','tv',50000)
emp_2= Employee('test','testing',30000)


# print(len(emp_1))
# print(emp_1+emp_2)

#len  is using special method


# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2))
# print(str.__add__('a','b'))

# special methods - to implement operator overloading
#surronded by double under score __ 
# unambigious rep  repr
# __repr__ 		for developer
# __str__		 for end user 


