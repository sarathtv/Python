#inheritance


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
		


class Developer(Employee):

	raise_amount=1.10

	def __init__(self,first,last,pay,prog_lang):
		#instead of copy and paste ,we will set only prog lang
		super().__init__(first,last,pay)# parent class will init these
		#Employee.__init__(self,first,last,pay) # both are valid... but other is preferred
		self.prog_lang=prog_lang

class Manager(Employee):
			"""docstring for ClassName"""
			def __init__(self,first,last,pay,employees=None):
				super().__init__(first,last,pay)
				if employees is None:
					self.employees=[]
				else:
				    self.employees=employees	

			def add_emp(self,emp):
				if emp not in self.employees:
					self.employees.append(emp)

					
	
			def remove_emp(self,emp):
				if emp  in self.employees:
					self.employees.remove(emp)
					

			def print_emps(self):
				for emp  in self.employees:
					print('--->' , emp.fullname())
					
emp_1 =Employee('sarath','tv',50000)
emp_2= Employee('test','testing',30000)

emp_3= Developer('test','testing',50000,'python')


mgr_1=Manager('Stv','tvs',95000,[emp_3])
# print(mgr_1.email)
# mgr_1.print_emps()

print(isinstance(mgr_1,Employee))
print(issubclass(Manager,Employee))



#method resolution function

#print(help(Developer))


# print(emp_1.email)
# print(emp_3.email)
# print(emp_3.prog_lang)
# 
# print(emp_3.pay)
# emp_3.apply_raise()
# print(emp_3.pay)
