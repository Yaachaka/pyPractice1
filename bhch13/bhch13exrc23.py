"""
bhch13exrc23.py: Write a function that is given a 9 x 9 potentially solved Sudoku and returns True if it is solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are no repeated numbers in any row or any column or in any of the nine "blocks".
"""
print('*'*80)

from pprint import pprint

sudoku = []

def read_row(i):
	while True:
		row = input('Enter row {:}: '.format(i))[:9]
		if len(row) == 9:
			if '0' in row:
				print('Invalid digits... Enter again')
			else:
				sudoku.append(list(row))
				break
		else:
			print('Not enough or more number of digits in row. Enter a again.')
	
def read_table():
	print('Enter each row in format \'xxxxxxxxx\'.')
	for i in range(9):
		read_row(i)

def check(s):
	flag = 0
	for i in s:
		for j in i:
			if i.count(j) != 1:
				flag = 1
				break
		if flag:
			break
	return not flag

print('Enter sudoku table: ')
read_table()

t_sudoku = [[sudoku[j][i] for j in range(9)] for i in range(9)]

if check(sudoku) and check(t_sudoku):
	print('The sudoku puzzle is correctly solved.')
else:
	print('The solution is not correct.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter sudoku table:
Enter each row in format 'xxxxxxxxx'.
Enter row 0: 435269781
Enter row 1: 6825714933
Enter row 2: 19783456
Not enough or more number of digits in row. Enter a again.
Enter row 2: 197834562
Enter row 3: 826195347
Enter row 4: 374682915
Enter row 5: 951743628
Enter row 6: 519326874
Enter row 7: 248957136
Enter row 8: 763418259
The sudoku puzzle is correctly solved.
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter sudoku table:
Enter each row in format 'xxxxxxxxx'.
Enter row 0: 432569781
Enter row 1: 682571493
Enter row 2: 197834562
Enter row 3: 826195347
Enter row 4: 374682915
Enter row 5: 981743628
Enter row 6: 519326874
Enter row 7: 248957136
Enter row 8: 763418259
The solution is not correct.
********************************************************************************
"""