"""
bhch14exrc09.py: Write a class called Rock_paper_scissors that implements the logic of the game Rockpaper-scissors. For this game the user plays against the computer for a certain number of rounds. Your class should have fields for the how many rounds there will be, the current round number, and the number of wins each player has. There should be methods for getting the computer’s choice, finding the winner of a round, and checking to see if someone has one the (entire) game. You may want more methods.
"""
print('*'*80)
#------------------------------------------------------------------------------
from random import randint
#------------------------------------------------------------------------------
class Rock_paper_scissors:
	def __init__(self, n_rounds):
		self.n_rounds =  n_rounds
		self.current_round = 0
		self.p1_wins = 0
		self.p2_wins = 0
		self.ties = 0

	def computer_choice(self):
		return randint(0, 2)

	def round_win(self, p1, p2):
		if p1 == p2:
			self.ties += 1
		elif (p1 == 0 and p2 == 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0):
			self.p2_wins += 1
		else:
			self.p1_wins += 1
		
	def result(self, p1, p2):
		print('Winner: ', end='')
		if self.p1_wins == self.p2_wins:
			print('Its a tie.')
		elif self.p1_wins > self.p2_wins:
			print(p1)
		else:
			print(p2)
		
		print('\nGame stats:')
		print('Player {:}: {:}'.format(p1, self.p1_wins))
		print('Player {:}: {:}'.format(p2, self.p2_wins))
		print('Ties: {:}'.format(self.ties))
#------------------------------------------------------------------------------
rps = ['Rock', 'Paper', 'Scissor']
n_rounds = eval(input('How many rounds (max = 10): '))%10
if not n_rounds:
	n_rounds = 10

game1 = Rock_paper_scissors(n_rounds)
for i in range(n_rounds):
	game1.current_round = i+1
	print('Round:', i+1)

	p1 = eval(input('Choose: 0 - Rock, 1 - Paper, 2 - Scissor: '))%3
	p2 = game1.computer_choice()
	print('{} : {}'.format(rps[p1], rps[p2]))
	game1.round_win(p1, p2)
	print()

game1.result('You', 'Computer')
#------------------------------------------------------------------------------

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
How many rounds (max = 10): 6
Round: 1
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 2
Scissor : Rock

Round: 2
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 1
Paper : Rock

Round: 3
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 4
Paper : Paper

Round: 4
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 2
Scissor : Scissor

Round: 5
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 4
Paper : Rock

Round: 6
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 1
Paper : Scissor

Winner: Its a tie.

Game stats:
Player You: 2
Player Computer: 2
Ties: 2
********************************************************************************

@@@@ Trial2:
********************************************************************************
How many rounds (max = 10): 1
Round: 1
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 2
Scissor : Scissor

Winner: Its a tie.

Game stats:
Player You: 0
Player Computer: 0
Ties: 1
********************************************************************************

@@@@ Trial3:
********************************************************************************
How many rounds (max = 10): 4
Round: 1
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 1
Paper : Paper

Round: 2
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 2
Scissor : Rock

Round: 3
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 3
Rock : Scissor

Round: 4
Choose: 0 - Rock, 1 - Paper, 2 - Scissor: 1
Paper : Rock

Winner: You

Game stats:
Player You: 2
Player Computer: 1
Ties: 1
********************************************************************************
"""