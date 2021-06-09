#---------------------------INCOMPLETE--------------------------------------

"""
bhch08exrc25.py: Here is an old puzzle question you can solve with a computer program. There is only one five-digit number n that is such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find n.

01265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414
"""
print('*'*80)

given = [1265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 39414]

l1 = [list(str('%.5d'%given[i])) for i in range(len(given))]

print(l1)

number = 00000
stop = 0
counter = 0
for i in range(0,100000):
	l2 = list(str('%.5d'%i))
	for j in range(len(given)): # Loop through each of the given number
		l3 = l1[j]
		no_digit = 1
		counter = counter + 1
		for k in range(len(l3)):  # Loop through in search of digits in selected number 
			if l3.count(l2[k]) == 1:  # If atleast one digit is present
				ind = l3.index(l2[k])
				if l2[ind] == l3[ind]: #check if they reside at same position.
					no_digit = 0
					break
		if no_digit: # One of the given number doesn't contain a digit in i.
			break
		if j == len(given)-1:
			stop = 1
	if stop:  # Number found... Lets break from the outermost loop
		break

print('The number is', '%.5d'%number)

print('*'*80)
"""PROGRAM OUTPUT

"""
