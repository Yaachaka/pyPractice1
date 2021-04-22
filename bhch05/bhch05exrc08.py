"""
@@@@ Program Statement:
Write a program that swaps the values of three variables x, y, and z, 
so that x gets the value of y, y gets the value of z, and z gets 
the value of x.
"""
x=5
y=10
z=15
print('Before swapping: x=', x, 'y=', y, 'z=', z)
x, y, z = y, z, x
print('After swapping: x=', x, 'y=', y, 'z=', z)