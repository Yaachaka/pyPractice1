from random import randint

print(randint(1,2), end='')
for i in range(3, 52):
	print(', ', randint(1, i), sep='', end='')