"""
bhch06exrc24.py:
In calculus, the derivative of x<sup>4</sup> is 4x<sup>3</sup>. The derivative of x<sup>5</sup> is 5x<sup>4</sup>. The derivative of x<sup>6</sup> is 
6x<sup>5</sup>. This pattern continues. Write a program that asks the user for input like x^3 or x^25
and prints the derivative. For example, if the user enters x^3, the program should print out
3x^2.
"""
print('*'*80)

polynomial = input('Enter polynomial (x^p, p is integer): ')

power = int(polynomial[polynomial.index('^') + 1:])
derivative = str(power) + 'x^' + str(power-1)

print('Derivative is', derivative)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter polynomial (x^p, p is integer): x^3
Derivative is 3x^2
********************************************************************************
@@@@ Trial2:
********************************************************************************
Enter polynomial (x^p, p is integer): x^34
Derivative is 34x^33
********************************************************************************
"""