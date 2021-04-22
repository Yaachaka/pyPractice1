"""
bhch06exrc10.py
Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH  
EE  
YY
"""
print('*'*80)
string = input('Enter a string: ')

for c in string:
	print(c*2)

print('*'*80)

"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter a string: HEy
HH
EE
yy
********************************************************************************

Trial2:
********************************************************************************
Enter a string: Learning PYTHON!!!
LL
ee
aa
rr
nn
ii
nn
gg

PP
YY
TT
HH
OO
NN
!!
!!
!!
********************************************************************************
"""