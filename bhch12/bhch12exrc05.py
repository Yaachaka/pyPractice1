"""
bhch12exrc05.py: You are given a file namelist.txt that contains a bunch of names. Some of the names are a first name and a last name separated by spaces, like George Washington, while others have a middle name, like John Quincy Adams. There are no names consisting of just one word or more than three words. Write a program that asks the user to enter initials, like GW or JQA, and prints all the names that match those initials. Note that initials like JA should match both John Adams and John Quincy Adams.
"""
print('*'*80)

file1 = [line.strip().split(' ') for line in open('namelist.txt')]

abbr_name = input('Enter initials to list out the names: ')
for i in file1:
	if abbr_name[:2].upper() == i[0][0].upper() + i[-1][0].upper():
		print(' '.join(i))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter initials to list out the names: ab
Alan James Bond
Alan Brewster
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter initials to list out the names: jl
Jhansi Rani Lakshmibai
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter initials to list out the names: al
Abraham Lincon
********************************************************************************

@@@@ Trial4:
********************************************************************************
Enter initials to list out the names: JA
John Quincy Adams
James Anderson
********************************************************************************
"""