"""
bhch07exrc06.py: Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.
"""
print('*'*80)

alist = []
listsqr = []
listletters = []
alphas = 'abcdefghijklmnopqrstuvwxyz'

for i in range(50):
	alist = alist + [i]
	listsqr = listsqr + [(i+1)*(i+1)]
	if i < 26:
		listletters = listletters + [alphas[i] * (i+1)]

print('List containing integers 0 through 49:', alist)
print('\nList containing the squares of the integers 1 through 50:', listsqr)
print('\nThe list [\'a\',\'bb\',\'ccc\',\'dddd\', ...] that ends with 26 copies of the letter z:', listletters)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
List containing integers 0 through 49: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

List containing the squares of the integers 1 through 50: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729,
784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500]

The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq', 'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu', 'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx', 'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz']
********************************************************************************
"""