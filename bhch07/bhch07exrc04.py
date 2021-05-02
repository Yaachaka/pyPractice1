"""
bhch07exrc04.py: Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10.
"""
print('*'*80)

list1 = eval(input('Enter a list containing elements between 1 and 12: '))
for i in range(len(list1)):
	if list1[i] > 10:
		list1[i] = 10
	if list1[i] < 1:
		list1[i] = 1

print('Tuned list:', list1)
print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a list containing elements between 1 and 12: [1, 2, 0, 12, 5, 45, 56, 3, 4, 9]
Tuned list: [1, 2, 1, 10, 5, 10, 10, 3, 4, 9]
********************************************************************************
"""