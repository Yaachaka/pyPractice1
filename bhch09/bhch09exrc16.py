"""
bhch09exrc16.py: Write a text-based version of the game Memory. The game should generate a 5 x 5 board (see the exercise from Chapter 8). Initially the program should display the board as a 5 x 5 grid of asterisks. The user then enters the coordinates of a cell. The program should display the grid with the character at those coordinates now displayed. The user then enters coordinates of another cell. The program should now display the grid with the previous character and the new character displayed. If the two characters match, then they should permanently replace the asterisks in those locations. Otherwise, when the user enters the next set of coordinates, those characters should be replaced by asterisks. The game continues this way until the player matches everything or runs out of turns. You can decide how many turns they player gets.
"""
print('*'*80)

from random import shuffle, sample

chars = 'ABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&()'
few1 = sample(list(chars), 18)
few2 = few1 * 2
shuffle(few2)

#Puzzle is created and stored
mat = [few2[i:i+6] for i in range(0,36,6)]
mat2 = [['*']*6 for j in range(6)]  #Closed puzzle
#print(mat)
#print(mat2)
#Print '*' matrix 
for i in range(6):
		print('* '*6)
	
	
#User interaction
print('You get to choose wrong tiles only 10 times. Let\'s play... ')
miss = 10
while miss:
	#Get first postion
	x1 = eval(input('Enter x co-ordinate(0-5): '))%6
	y1 = eval(input('Enter y co-ordinate(0-5): '))%6
	if mat2[x1][y1] == '*': #If the position is still locked proceed
		mat2[x1][y1] = mat[x1][y1] #Unlock the cell and display the character
		for i in range(6):
			for j in range(6):
				print(mat2[i][j], end=' ')
			print()
		#Get the position of the next cell
		unlocked = 1
		while unlocked: 
			x2 = eval(input('Enter 2nd x co-ordinate(0-5): '))%6
			y2 = eval(input('Enter 2nd y co-ordinate(0-5): '))%6
			if mat2[x2][y2] == '*': #If the position is still locked proceed
				unlocked = 0
				mat2[x2][y2] = mat[x2][y2] #Unlock the cell and display the character
				for i in range(6):
					for j in range(6):
						print(mat2[i][j], end=' ')
					print()
				#Now check if the two cells match with their characters
				if mat2[x1][y1] == mat2[x2][y2]: #If they match, good
					print('Not bad!!!')
				else: #if they do not match, display the status of the puzzle and proceed
					mat2[x1][y1] = mat2[x2][y2] = '*'
					miss = miss -1
					print(':(:(:(', miss, 'chances left.')
					for i in range(6):
						for j in range(6):
							print(mat2[i][j], end=' ')
						print()
					
			else:
				print('That tile is already open. Try again.')
				
	else: #Else print that the cell is already open.
		print('That tile is already open. Try again.')

temp = [j for i in mat2 for j in i]

if temp.count('*'):
	print('Game incomplete. You lose')
else:
	print('You win!!! Congratulations...')

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
You get to choose wrong tiles only 10 times. Let's play...
Enter x co-ordinate(0-5): 4
Enter y co-ordinate(0-5): 4
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * O *
* * * * * *
Enter 2nd x co-ordinate(0-5): 1
Enter 2nd y co-ordinate(0-5): 1
* * * * * *
* I * * * *
* * * * * *
* * * * * *
* * * * O *
* * * * * *
:(:(:( 9 chances left.
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 0
Enter y co-ordinate(0-5): 0
X * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 2
Enter 2nd y co-ordinate(0-5): 2
X * * * * *
* * * * * *
* * B * * *
* * * * * *
* * * * * *
* * * * * *
:(:(:( 8 chances left.
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 3
Enter y co-ordinate(0-5): 3
* * * * * *
* * * * * *
* * * * * *
* * * V * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 5
Enter 2nd y co-ordinate(0-5): 5
* * * * * *
* * * * * *
* * * * * *
* * * V * *
* * * * * *
* * * * * N
:(:(:( 7 chances left.
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 4
Enter y co-ordinate(0-5): 3
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * # * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 2
Enter 2nd y co-ordinate(0-5): 3
* * * * * *
* * * * * *
* * * B * *
* * * * * *
* * * # * *
* * * * * *
:(:(:( 6 chances left.
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 2
Enter y co-ordinate(0-5): 2
* * * * * *
* * * * * *
* * B * * *
* * * * * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 2
Enter 2nd y co-ordinate(0-5): 3
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Not bad!!!
Enter x co-ordinate(0-5): 4
Enter y co-ordinate(0-5): 5
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * C
* * * * * *
Enter 2nd x co-ordinate(0-5): 1
Enter 2nd y co-ordinate(0-5): 2
* * * * * *
* * R * * *
* * B B * *
* * * * * *
* * * * * C
* * * * * *
:(:(:( 5 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 3
Enter y co-ordinate(0-5): 1
* * * * * *
* * * * * *
* * B B * *
* $ * * * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 5
Enter 2nd y co-ordinate(0-5): 1
* * * * * *
* * * * * *
* * B B * *
* $ * * * *
* * * * * *
* & * * * *
:(:(:( 4 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 3
Enter y co-ordinate(0-5): 4
* * * * * *
* * * * * *
* * B B * *
* * * * P *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 2
Enter 2nd y co-ordinate(0-5): 1
* * * * * *
* * * * * *
* R B B * *
* * * * P *
* * * * * *
* * * * * *
:(:(:( 3 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 3
Enter y co-ordinate(0-5): 2
* * * * * *
* * * * * *
* * B B * *
* * U * * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 5
Enter 2nd y co-ordinate(0-5): 3
* * * * * *
* * * * * *
* * B B * *
* * U * * *
* * * * * *
* * * M * *
:(:(:( 2 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 2
Enter y co-ordinate(0-5): 4
* * * * * *
* * * * * *
* * B B X *
* * * * * *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 3
Enter 2nd y co-ordinate(0-5): 5
* * * * * *
* * * * * *
* * B B X *
* * * * * &
* * * * * *
* * * * * *
:(:(:( 1 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Enter x co-ordinate(0-5): 2
Enter y co-ordinate(0-5): 2
That tile is already open. Try again.
Enter x co-ordinate(0-5): 3
Enter y co-ordinate(0-5): 4
* * * * * *
* * * * * *
* * B B * *
* * * * P *
* * * * * *
* * * * * *
Enter 2nd x co-ordinate(0-5): 4
Enter 2nd y co-ordinate(0-5): 4
* * * * * *
* * * * * *
* * B B * *
* * * * P *
* * * * O *
* * * * * *
:(:(:( 0 chances left.
* * * * * *
* * * * * *
* * B B * *
* * * * * *
* * * * * *
* * * * * *
Game incomplete. You lose
********************************************************************************
"""