"""
@@@@ Program statement: bhch05exrc14.py
This exercise is about the well-known Monty Hall problem. In the problem, 
you are a contestant on a game show. The host, Monty Hall, shows you 
three doors. Behind one of those doors is a prize, and behind the other 
two doors are goats. You pick a door. Monty Hall, who knows behind 
which door the prize lies, then opens up one of the doors that doesn’t 
contain the prize. There are now two doors left, and Monty gives you 
the opportunity to change your choice. Should you keep the same door, 
change doors, or does it not matter?  
(a) Write a program that simulates playing this game 10000 times and 
calculates what percentage of the time you would win if you switch and 
what percentage of the time you would win by not switching.  
(b) Try the above but with four doors instead of three. There is still 
only one prize, and Monty still opens up one door and then gives you 
the opportunity to switch.
"""

print('WELCOME TO MONTY HALL PROBLEM CONTEST')
print('There are 3 door and 4 door games.')
print('Each door to each room.')
print('One of the room contains a big prize and the remaining contain goats.')
print('Let us see how lucky you are today!!!')

from random import randint

doors = eval(input('Enter 1 to choose 4 door game, otherwise to choose 3 door game: '))
if doors == 1:
	doors = 4
else:
	doors = 3

sw_count = 0
win_count = 0
sw_count_win = 0

print()

for i in range(5):
	print('Trial ', i+1, ':')
	guess = eval(input('Choose your door: '))
	if 1 <= guess <= doors:
		gift = randint(1, doors)
		if doors == 1:  #4 door game
			if gift == 1:
				goat1 = 2
				goat2 = 3
				goat3 = 4
			elif gift == 2:
				goat1 = 3
				goat2 = 4
				goat3 = 1
			elif gift == 3:
				goat1 = 4
				goat2 = 1
				goat3 = 2
			else:
				goat1 = 1
				goat2 = 2
				goat3 = 3
			print('Well, you chose the door. Lets make the contest more interesting.')
			if(guess == goat1 and goat2 != gift):
				open = goat2
			elif(guess == goat2 and goat3 != gift):
				open = goat3
			elif(guess == goat3 and goat4 != gift):
				open = goat4
			else:
				open = goat1
			print('Let us open a door!!!')
			print('Let us open the door',open)
			print('Ohh... It contains goat.')
			print()
			print('I will give you a chance to change your choice.')

		else:  #3 door game
			if(gift == 1):
				goat1 = 2
				goat2 = 3
			elif(gift == 2):
				goat1 = 3
				goat2 = 1
			else:
				goat1 = 1
				goat2 = 2
			print('Well, you chose the door. Lets make the contest more interesting.')
			if(guess == goat1):
				open = goat2
			else:
				open = goat1
			print('Let us open a door!!!')
			print('Let us open the door',open)
			print('Ohh... It contains goat.')
			print()
			print('I will give you a chance to change your choice.')

		print('Choose a door between the', doors - 1, 'remaining doors: ', end='')
		switch = eval(input())

		if((switch != open) and 1 <= switch <= doors):
			old_guess = guess
			if(switch != guess):
				sw_count = sw_count + 1
			guess = switch
			if(guess == gift):
				print('WONDERFULLL... You are so lucky today. You got the prize.')
				win_count = win_count + 1
				if(switch != old_guess):
					sw_count_win = sw_count_win + 1
			else:
				print('Oh.. sad. you get a goat.')
		else:
			print('You must be drunk. You better step out of the contest.')
			print('You lose a trial. Let us continue.')
	else:
		print('You piggg!!! Choose from available.')
		print('You lose a trial. Let us continue.')
	print()
	print()

#Result
if(win_count==5):
	print('WOWWW... You are in total luck today.')
print('You switched your choice',sw_count,'times')
print('Total winning percentage:',win_count*100//5)
if sw_count != 0:
	print('Winning percentage when switched:',sw_count_win*100//sw_count)