"""
bhch11exrc11.py: In Section 6.10 we met the substitution cipher. This cipher replaces every letter with a different letter. For instance every a might be replaced with an e, every b might be replaced with an a, etc. Write a program that asks the user to enter two strings. Then determine if the second string could be an encoded version of the first one with a substitution cipher. For instance, CXYZ is not an encoded version of BOOK because O got mapped to two separate letters. Also, CXXK is not an encoded version of BOOK, because K got mapped to itself. On the other hand, CXXZ would be an encoding of BOOK. This problem can be done with or without a dictionary.
"""
print('*'*80)

msg1 = {}

message1 = input('Enter message1: ')
message2 = input('Enter message2: ')

cipherable = 0
if len(message1) == len(message2):
	for i in range(len(message1)):
		if message1[i] in msg1:
			if msg1[message1[i]] != message2[i]:
				break
		else:
			if message1[i] == message2[i]:#To avoid a character mapping on to itself
				break
			if message2[i] in list(msg1.values()):#To avoid same character to map on to two different characters.
				break
			else:
				msg1[message1[i]] = message2[i]#Add new mapping to the dictionary.
	else:
		cipherable = 1

if cipherable:
	print('Yes, the messages can be encrypted with substitution cipher.')
else:
	print('No, the messages cannot be encrypted with substitution cipher.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter message1: cxyz
Enter message2: book
No, the messages cannot be encrypted with substitution cipher.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter message1: cxxk
Enter message2: book
No, the messages cannot be encrypted with substitution cipher.
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter message1: cxxz
Enter message2: book
Yes, the messages can be encrypted with substitution cipher.
********************************************************************************

@@@@ Trial4:
********************************************************************************
Enter message1: booked tickets!!
Enter message2: ammlbcsqjdlbq ??
Yes, the messages can be encrypted with substitution cipher.
********************************************************************************
"""