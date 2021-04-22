"""
bhch06exrc25.py:
In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5).
Computers prefer those expressions to include the multiplication symbol, like 3*x+4*y or
3*(x+5). Write a program that asks the user for an algebraic expression and then inserts
multiplication symbols where appropriate.
"""
print('*'*80)

exp = input('Enter arithmetic expression: ')

exp2 = exp[0]
for i in range(1, len(exp)):
	if exp[i] == '(':
		if exp[i-1] in '0123456789x':
			exp2 = exp2 + '*'
	elif exp[i] == 'x':
		if exp[i-1] in '0123456789':
			exp2 = exp2 + '*'
	exp2 = exp2 + exp[i]

print('Rewritten expression:', exp2)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter arithmetic expression: 3x+4(x+y)
Rewritten expression: 3*x+4*(x+y)
********************************************************************************
@@@@ Trial2:
********************************************************************************
Enter arithmetic expression: 3(x+5)
Rewritten expression: 3*(x+5)
********************************************************************************
@@@@ Trial3:
********************************************************************************
Enter arithmetic expression: 3+4x-8
Rewritten expression: 3+4*x-8
********************************************************************************
@@@@ Trial4:
********************************************************************************
Enter arithmetic expression: x+4x*x
Rewritten expression: x+4*x*x
********************************************************************************
"""