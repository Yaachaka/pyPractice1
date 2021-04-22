"""
bhch06exrc14.py:
Write a program that asks the user to enter their name in lowercase and then capitalizes the
first letter of each word of their name.
"""
print('*'*80)

name = input('Enter your name in lowercase: ')

name = name[0].upper() + name[1:]
print('Your name stored as:', name)

print('*'*80)


"""PROGRAM OUTPUT:
Trial1:
********************************************************************************
Enter your name in lowercase: govinda
Your name stored as: Govinda
********************************************************************************

Trial2:
********************************************************************************
Enter your name in lowercase: bhoomi
Your name stored as: Bhoomi
********************************************************************************
"""