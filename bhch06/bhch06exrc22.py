"""
bhch06exrc22.py:
A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
characters is to pick out the characters at even indices, put them first in the encrypted string,
and follow them by the odd characters. For example, the string *message* would be encrypted
as *msaeesg* because the even characters are *m*, *s*, *a*, *e* (at indices 0, 2, 4, and 6) and the odd
characters are *e*, *s*, *g* (at indices 1, 3, and 5).  
(a) Write a program that asks the user for a string and uses this method to encrypt the string.  
(b) Write a program that decrypts a string that was encrypted with this method.  
"""
print('*'*80)

message = input('Enter a message: ')
length = len(message)
halflength = length//2

encrypted = ''
decrypted = ''
evens = ''
odds = ''

#encrypting
for i in range(0,halflength*2,2):
	evens = evens + message[i]
	odds = odds + message[i+1]

if length%2:
	evens = evens + message[-1]

encrypted = evens + odds

print('Encrypted message:', encrypted)

#decrypting
for i in range(halflength):
	decrypted = decrypted + encrypted[i] + encrypted[i-halflength]

if length%2:
	decrypted = decrypted + encrypted[halflength]

print('Decrypted message:', decrypted)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a message: I am not going there.
Encrypted message: Ia o on hr. mntgigtee
Decrypted message: I am not going there.
********************************************************************************
"""