"""
bhch14exrc01.py: Write a class called Investment with fields called principal and interest. The constructor should set the values of those fields. There should be a method called value_after that returns the value of the investment after n years. The formula for this is p(1 + i)n, where p is the principal, and i is the interest rate. It should also use the special method __str__ so that printing the object will result in something like below:

	Principal - $1000.00, Interest rate - 5.12%
"""
print('*'*80)

class Investment:
	def __init__(self, principal, interest):#Constructor
		self.principal = principal
		self.interest = interest
	
	def value_after(self, n):
		return principal*(1 + interest)**n
	
	def __str__(self):
		return ('Principal - ${:}, Interest rate - {:}%'.format(principal, interest))

principal = eval(input('Enter principal amount: '))
interest = eval(input('Enter interest rate: '))
n_years = eval(input('Enter no. of years: '))
inv1 = Investment(principal, interest)
print(inv1)

print('Investment after {:} years is {:}.'.format(n_years, inv1.value_after(n_years)))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter principal amount: 100000.12
Enter interest rate: 5.43
Enter no. of years: 5
Principal - $100000.12, Interest rate - 5.43%
Investment after 5 years is 1099146005.088053.
********************************************************************************
"""