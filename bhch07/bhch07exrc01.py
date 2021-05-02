"""
bhch07exrc01.py: 
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the result.
(g) Print how many integers in the list are less than 5.
"""
print('*'*80)

list = eval(input('Enter a list of integers: '))

print('(a) Total number of items in the list:', len(list))
print('(b) Last item in the list:', list[-1])
print('(c) List in reverse order: ', list[::-1])#list.reverse()
print('(d) Does the list contains element as 5?: ', end='')
if list.count(5):
	print('Yes')
else:
	print('No')
print('(e) Number of fives in the list:', list.count(5))

list2 = list[1:-1]
list2.sort()
print('(f) The 1st & last items are removed and the remaining are sorted.')
print('\t', list2)

count = 0
for i in list:
	if i < 5:
		count = count + 1
print('(g) The number of items that are less than 5 is', count)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter a list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
(a) Total number of items in the list: 19
(b) Last item in the list: 1
(c) List in reverse order:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
(d) Does the list contains element as 5?: Yes
(e) Number of fives in the list: 2
(f) The 1st & last items are removed and the remaining are sorted.
         [0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
(g) The number of items that are less than 5 is 9
********************************************************************************
"""