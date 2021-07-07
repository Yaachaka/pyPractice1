"""
bhch14exrc10.py: (a) Write a class called Connect4 that implements the logic of a Connect4 game. Use the Tic_tac_toe class from this chapter as a starting point.
(b) Use the Connect4 class to create a simple text-based version of the game.
"""
print('*'*80)

#------------------------------------------------------------------------------
from random import randint
#------------------------------------------------------------------------------
class Connect4:
	def __init__(self, nr=6, nc=7):
		self.nr = nr
		self.nc = nc
		self.B = [[0 for j in range(self.nc)] for i in range(self.nr)]#Board of 6 rows and 7 columns
		self.player = 1
	
	def get_open_spots(self):
		return [[r,c] for r in range(self.nr) for c in range(self.nc) if self.B[r][c]==0]
	
	def is_valid_move(self,r,c):
		if 0<=r<=self.nr and 0<=c<=self.nc and self.B[r][c]==0:
			return True
		return False
	
	def make_move(self,r,c):
		if self.is_valid_move(r,c):
			self.B[r][c] = self.player
			self.player = (self.player+2)%2 + 1
	
	def check_for_winner(self):
		b2 = [[str(self.B[r][c]) for c in range(self.nc)]for r in range(self.nr)]
		#Check in rows
		for i in b2:
			x = self.in_there(i)
			if x:
				return x
		#Check in cols
		cols = [[b2[c][r] for c in range(self.nr)] for r in range(self.nc)]
		for i in cols:
			x = self.in_there(i)
			if x:
				return x
		#Check in diagonals
		for r in range(self.nr):
			for c in range(self.nc-3):
				x = self.for_diag(b2, r, c, -1)#Diagonally up
				if x:
					return x
				x = self.for_diag(b2, r, c, 1)#Diagonally down
				if x:
					return x

		#If no player wins, it is a tie
		if self.get_open_spots()==[]:
			return 0
		return -1
	
	def in_there(self, i):
		x = ''.join(i)
		if '1111' in x:
			return 1
		if '2222' in x:
			return 2
		return 0
	
	def for_diag(self, b2, r, c, i):
		temp = ''
		r1, c1 = r, c
		while True:
			temp += b2[r1][c1]
			r1 += 1*i
			c1 += 1
			if not(0<=r1<self.nr and 0<=c1<self.nc):
				break
		x = self.in_there(temp)
		if x:
			return x
		else:
			return 0
			
#------------------------------------------------------------------------------
def print_board():
	chars = ['\u263c', '\u2658', '\u265e']#['-', 'X', 'O']#☼, ♘, ♞
	print(' '*3, end = '')
	for i in range(len(game.B[0])):
		print('{:2}'.format(i), end='')
	print()
	for r in range(6):
		print('{:2}|'.format(r), end=' ')
		for c in range(7):
			print(chars[game.B[r][c]], end=' ')
		print()
#------------------------------------------------------------------------------
game = Connect4()
while game.check_for_winner()==-1:
	print_board()
	print('-'*15)
	p = game.player
	#r,c = eval(input('Enter spot, player {:}({:}): '.format(p, ['\u2658', '\u2653'][p-1]))
	r, c = randint(0, 5), randint(0, 6)
	print('Enter spot, player {:}({:}): {:}, {:}'.format(p, ['\u2658', '\u265e'][p-1], r, c))
	game.make_move(r,c)

print_board()
x = game.check_for_winner()
if x==0:
	print("It's a draw.")
else:
	print('Player', x, 'wins!')
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 0
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♘ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 3, 0
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♘ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 3, 2
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♘ ☼ ♞ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 3, 3
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 5, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 5
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 0, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 1, 4
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 2, 1
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 2, 6
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 4, 2
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 0, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ☼
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 4, 6
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 0, 3
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 1
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ☼ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 4, 4
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ☼ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 1, 5
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 6
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ☼ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 4, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 3, 0
    0 1 2 3 4 5 6
 0| ♞ ☼ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 0, 1
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ☼ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 5
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 4, 4
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 1, 3
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ♞ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ☼ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 2, 4
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ☼ ☼ ♞ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ♘ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 2(♞): 1, 1
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ♞ ☼ ♞ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ♘ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 3
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ♞ ☼ ♞ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ♘ ♘ ♞
 3| ♘ ♘ ♞ ♞ ☼ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 3, 4
    0 1 2 3 4 5 6
 0| ♞ ♞ ☼ ♞ ☼ ☼ ☼
 1| ☼ ♞ ☼ ♞ ♘ ♞ ☼
 2| ♘ ♘ ☼ ☼ ♘ ♘ ♞
 3| ♘ ♘ ♞ ♞ ♘ ♘ ☼
 4| ♘ ☼ ♞ ☼ ♘ ☼ ♘
 5| ☼ ♞ ☼ ☼ ☼ ☼ ☼
Player 1 wins!
********************************************************************************

@@@@ Trial2:
********************************************************************************
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ☼ ☼
---------------
Enter spot, player 1(♘): 5, 5
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 2(♞): 4, 4
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 1(♘): 3, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 2(♞): 3, 0
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ☼ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 1(♘): 4, 5
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 2(♞): 0, 6
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 1(♘): 2, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ☼
---------------
Enter spot, player 2(♞): 5, 6
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ☼ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 3, 4
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ☼ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 1, 1
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 4, 5
    0 1 2 3 4 5 6
 0| ☼ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 0, 0
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 4, 5
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ☼ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 1, 0
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 5, 5
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ☼ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 5, 3
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ☼ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 1, 2
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ♞ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 3, 1
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ♞ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ☼ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
---------------
Enter spot, player 1(♘): 4, 2
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ♞ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ♘ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 5, 5
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ♞ ☼ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ♘ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
---------------
Enter spot, player 2(♞): 1, 3
    0 1 2 3 4 5 6
 0| ♘ ☼ ☼ ☼ ☼ ☼ ♞
 1| ♞ ♞ ♞ ♞ ☼ ☼ ☼
 2| ☼ ♘ ☼ ☼ ☼ ☼ ☼
 3| ♞ ♘ ☼ ☼ ♘ ☼ ☼
 4| ☼ ☼ ♘ ☼ ♞ ♘ ☼
 5| ☼ ☼ ☼ ♘ ☼ ♘ ♞
Player 2 wins!
********************************************************************************
"""