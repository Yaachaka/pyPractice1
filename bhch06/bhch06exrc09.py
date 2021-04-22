"""
bhch06exrc09.py
Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
 1
  2
   3
    4
"""
print('*'*80)

num = eval(input('Enter a number: '))

for i in range(num):
	print(' '*(i+1), i+1, sep='')

print('*'*80)

"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter a number: 5
 1
  2
   3
    4
     5
********************************************************************************

Trial2:
********************************************************************************
Enter a number: 9
 1
  2
   3
    4
     5
      6
       7
        8
         9
********************************************************************************
"""