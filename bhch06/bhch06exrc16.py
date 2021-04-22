"""
bhch06exrc16.py:
Companies often try to personalize their offers to make them more attractive. One simple
way to do this is just to insert the person’s name at various places in the offer. Of course,
companies don’t manually type in every person’s name; everything is computer-generated.
Write a program that asks the user for their name and then generates an offer like the one
below. For simplicity’s sake, you may assume that the person’s first and last names are one
word each.
	Enter name: George Washington  
	Dear George Washington,  

	I am pleased to offer you our new Platinum Plus Rewards card
	at a special introductory APR of 47.99%. George, an offer
	like this does not come along every day, so I urge you to call
	now toll-free at 1-800-314-1592. We cannot offer such a low
	rate for long, George, so call right away.
"""
print('*'*80)

name = input('Enter name: ')
i = name.index(' ')
firstName = name[:i]
lastName = name[i+1:]

print('Dear ',firstName, ' ', lastName, ',', sep='')  
print()
print('I am pleased to offer you our new Platinum Plus Rewards card')
print('at a special introductory APR of 47.99%. ', firstName, ', an offer', sep='')
print('like this does not come along every day, so I urge you to call')
print('now toll-free at 1-800-314-1592. We cannot offer such a low')
print('rate for long, ', firstName, ', so call right away.', sep='')

print('*'*80)

"""PROGRAM OUTPUT
Trial1:
********************************************************************************
Enter name: Marie Curie
Dear Marie Curie,

I am pleased to offer you our new Platinum Plus Rewards card
at a special introductory APR of 47.99%. Marie, an offer
like this does not come along every day, so I urge you to call
now toll-free at 1-800-314-1592. We cannot offer such a low
rate for long, Marie, so call right away.
********************************************************************************
"""