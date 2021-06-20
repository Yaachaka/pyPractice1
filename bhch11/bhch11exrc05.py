"""
bhch11exrc05.py: Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost. Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records.
"""
print('*'*80)

n = eval(input('Number of teams you want to add: '))
scoreboard = {}
#Getting data from user
while n:
	team_name = input('Enter team name: ').lower()
	if team_name in scoreboard:
		print('Team name already exists.')
	else:
		n -= 1
		team_wins = eval(input('Enter team\'s wins: '))
		team_loss = eval(input('Enter team\'s losses: '))
		scoreboard[team_name] = [team_wins, team_loss]

#Printing all data
print('\nScoreboard is as follows:')
print('{:15} {:4} {:4}'.format('Team name', 'Won', 'lost'))
print('-'*26)
for team in scoreboard:
	print('{:15} {:4} {:4}'.format(team, scoreboard[team][0], scoreboard[team][1]))
print('-'*26)

#Part a) of the question
print('\nPart (a):')
team_name = input('Enter team name to know it\'s winning percentage: ')
if team_name in scoreboard:
	print('The winning percentage of the team is {:}%.'.format(scoreboard[team_name][0]*100/sum(scoreboard[team_name])))
else:
	print('Team name not in the list.')

#Part b) of the question
print('\nPart (b):')
wins = [i[0] for i in list(scoreboard.values())]
print('List created with wins of each team:', wins)

#Part b) of the question
print('\nPart (c):')
score = eval(input('Enter winning criteria to consider is as a record: '))
print('\nScoreboard with winning records is as follows:')
print('{:15} {:4} {:4}'.format('Team name', 'Won', 'lost'))
print('-'*26)
for team in scoreboard:
	if score <= scoreboard[team][0]:
		print('{:15} {:4} {:4}'.format(team, scoreboard[team][0], scoreboard[team][1]))
print('-'*26)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Number of teams you want to add: 5
Enter team name: brazil
Enter team's wins: 12
Enter team's losses: 9
Enter team name: argentina
Enter team's wins: 8
Enter team's losses: 12
Enter team name: england
Enter team's wins: 15
Enter team's losses: 9
Enter team name: Brazil
Team name already exists.
Enter team name: America
Enter team's wins: 13
Enter team's losses: 12
Enter team name: Nigeria
Enter team's wins: 7
Enter team's losses: 18

Scoreboard is as follows:
Team name       Won  lost
--------------------------
brazil            12    9
argentina          8   12
england           15    9
america           13   12
nigeria            7   18
--------------------------

Part (a):
Enter team name to know it's winning percentage: nigeria
The winning percentage of the team is 28.0%.

Part (b):
List created with wins of each team: [12, 8, 15, 13, 7]

Part (c):
Enter winning criteria to consider is as a record: 10

Scoreboard with winning records is as follows:
Team name       Won  lost
--------------------------
brazil            12    9
england           15    9
america           13   12
--------------------------
********************************************************************************
"""