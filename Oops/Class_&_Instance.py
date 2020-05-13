#attributes and methods


class Employee:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.email=first+ '.'+last+ '@mail.com'
		self.pay=pay

	def fullname(self):
		return '{} {}'.format(self.first,self.last)



emp_1 =Employee('sarath','tv',20)
emp_2= Employee('test','testing',30)


print(emp_1.email)	 
print(emp_2.email)



# emp_1.first="sarath"
# emp_1.last="tv"
# emp_1.email='stv@mail.com'


# emp_2.first="test"
# emp_2.last="lst"
# emp_2.email='test@mail.com'


print(emp_1.first)	 
print(emp_2.first)

print('{} {}'.format(emp_1.first,emp_1.last))

print(emp_2.fullname())

#set attributes when instance are created

#same things
print(emp_1.fullname())
print(Employee.fullname(emp_1))


#self arg for  methods is required,,automatically  the instance is passed