"""
bhch08exrc20.py: Write a program that checks to see if a 4 x 4 list is a magic square. In a magic square, every row, column, and the two diagonals add up to the same value.
"""
print('*'*80)

magic_square = eval(input('Enter 4x4 matrix(list): '))

inverse = [[magic_square[j][i] for j in range(4)] for i in range(4)]

rows = [sum(i) for i in magic_square]
columns = [sum(i) for i in inverse]
diagonal1 = sum([magic_square[i][3-i] for i in range(4)])
diagonal2 = sum([magic_square[i][i] for i in range(4)])

l1 = rows + columns + [diagonal1] + [diagonal2]

if l1.count(diagonal1) == 10:
	print('The square is a magic square. The value is', diagonal1)
else:
	print('The square is not a magic square.')
	print('Sums of rows:', rows)
	print('Sums of columns:', columns)
	print('Sum of primary diagonal elements:', diagonal1)
	print('Sum of secondary diagonal elements:', diagonal2)

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter 4x4 matrix(l[[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
The square is not a magic square.
Sums of rows: [10, 10, 10, 10]
Sums of columns: [4, 8, 12, 16]
Sum of primary diagonal elements: 10
Sum of secondary diagonal elements: 10
********************************************************************************
@@@@ Trial2:
********************************************************************************
Enter 4x4 matrix(list): [[1,2,3,4],[2,3,4,1],[6,1,1,2],[1,4,2,3]]
The square is not a magic square.
Sums of rows: [10, 10, 10, 10]
Sums of columns: [10, 10, 10, 10]
Sum of primary diagonal elements: 10
Sum of secondary diagonal elements: 8
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter 4x4 matrix(list): [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
The square is a magic square. The value is 34
********************************************************************************"""