height = eval(input('Enter the height of the letter A: '))

j = height - 1

print(' '*j, '*', sep='')
j = j-1

lineNo = 2
betweenSpace = 1

for i in range(2, height//2+1):
	print(' '*j, '*', ' '*betweenSpace, '*', sep='')
	j = j-1
	betweenSpace = betweenSpace+2
	lineNo = lineNo+1

print(' '*j, '*'*height, sep='')
betweenSpace = height
j = j-1

for i in range(height//2):
	print(' '*j, '*', ' '*betweenSpace, '*', sep='')
	j = j-1
	betweenSpace = betweenSpace+2
	lineNo = lineNo+1
