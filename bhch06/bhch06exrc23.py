"""
bhch06exrc23.py:
A more general version of the above technique is the *rail fence cipher*, where instead of breaking things into evens and odds, they are broken up by threes, fours or something larger. For
instance, in the case of threes, the string *secret message* would be broken into three groups. The
first group is *sr sg*, the characters at indices 0, 3, 6, 9 and 12. The second group is *eemse*, the
characters at indices 1, 4, 7, 10, and 13. The last group is *ctea*, the characters at indices 2, 5, 8,
and 11. The encrypted message is *sr sgeemsectea*.  
(a) Write a program that asks the user for a string and uses the rail fence cipher in the threes
case to encrypt the string.  
(b) Write a decryption program for the threes case.  
(c) Write a program that asks the user for a string, and an integer determining whether to
break things up by threes, fours, or whatever. Encrypt the string using the rail-fence
cipher.  
(d) Write a decryption program for the general case.
"""
print('*'*80)

from math import ceil

message = input('Enter a message: ')
length = len(message)
encSize = eval(input('Enter encryprion size: '))

encLength = length // encSize
encLength2 = ceil(length / encSize)
extras = length - encSize * (length // encSize)

encrypted = ''
decrypted = ''

#encrypting
for i in range(encSize):
	for j in range(i, length, encSize):
		encrypted = encrypted + message[j]

print('Encrypted message:', encrypted)

#decrypting
for i in range(encLength2):
	extras1 = extras
	currPos = i
	for j in range(encSize):
			decrypted = decrypted + encrypted[currPos]
			if length == len(decrypted):
				break
			if extras1 > 0:
				currPos = currPos + encLength2
			else:
				currPos = currPos + encLength
			extras1 = extras1 - 1

print('Decrypted message:', decrypted)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 2
Encrypted message: golniogigt
Decrypted message: googlingit
********************************************************************************
@@@@ Trial2:
********************************************************************************
Enter a message: googlingit3
Enter encryprion size: 3
Encrypted message: ggntolg3oii
Decrypted message: googlingit3
********************************************************************************
@@@@ Trial3:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 4
Encrypted message: glioitongg
Decrypted message: googlingit
********************************************************************************
@@@@ Trial4:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 5
Encrypted message: gionoggilt
Decrypted message: googlingit
********************************************************************************
@@@@ Trial5:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 6
Encrypted message: gnogoigtli
Decrypted message: googlingit
********************************************************************************
@@@@ Trial6:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 7
Encrypted message: ggoiotglin
Decrypted message: googlingit
********************************************************************************
@@@@ Trial7:
********************************************************************************
Enter a message: googlingit
Enter encryprion size: 8
Encrypted message: giotogling
Decrypted message: googlingit
********************************************************************************
@@@@ Trial8:
********************************************************************************
Enter a message: I am not going there.
Enter encryprion size: 2
Encrypted message: Ia o on hr. mntgigtee
Decrypted message: I am not going there.
********************************************************************************
@@@@ Trial9:
********************************************************************************
Enter a message: I am not going there.
Enter encryprion size: 3
Encrypted message: Imogntr  toghean i e.
Decrypted message: I am not going there.
********************************************************************************
@@@@ Trial10:
********************************************************************************
Enter a message: I am not going there.
Enter encryprion size: 4
Encrypted message: I  nh. nggeaoo rmtite
Decrypted message: I am not going there.
********************************************************************************
@@@@ Trial11:
********************************************************************************
Enter a message: I am not going there.
Enter encryprion size: 5
Encrypted message: Inot. oihatnem gr g e
Decrypted message: I am not going there.
********************************************************************************
"""