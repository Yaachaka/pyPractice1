"""
bhch12exrc06.py: You are given a file namelist.txt that contains a bunch of names. Print out all the names in the list in which the vowels a, e, i, o, and u appear in order (with repeats possible). The first vowel in the name must be a and after the first u, it is okay for there to be other vowels. An example is Ace Elvin Coulson.
"""
print('*'*80)

print('Instead of \'namelist.txt\' we are using \'namelist_e06.txt\'')
file1 = [line.strip() for line in open('namelist_e06.txt')]
print('The names in the list in which the vowels appear in order:')

for x in file1:
	name = x.lower()#We are using x and name just retain camel casing of the name
	vow_list = []
	for j in 'aeiou':#Collect indices of vowels that appeared
		if j in name:
			vow_list.append(name.index(j))

	check = 1
	if vow_list[-1] != max(vow_list):
		check = 0
	else:
		for i in range(len(vow_list)-2):
			if vow_list[i] > vow_list[i+1]:
				check = 0
				break
	
	if check:
		print('-', x)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Instead of 'namelist.txt' we are using 'namelist_e06.txt'
The names in the list in which the vowels appear in order:
- Adam Anderson
- Ace Elvis Coulson
- Heinold
********************************************************************************
"""