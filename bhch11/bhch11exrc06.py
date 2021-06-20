"""
bhch11exrc06.py: Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2. Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].
"""
print('*'*80)

print('Enter game scores(format: team1 score1 - team2 score2):')
print('When done entering, type \'#\' and press \'Enter\'')
string = ''
scoreboard = {}
while True:
	#Get user input and format as needed
	string = input('>> ').lower()
	if string[0] == '#':
		break
	l = string.split(' ')
	del l[2]
	l[1] = int(l[1])
	l[3] = int(l[3])
	
	for i in range(0, 4, 2):
		if l[i] in scoreboard:
			scoreboard[l[i]][0] += l[i+1] #Add winning score to an existing one
			scoreboard[l[i]][1] += l[(i+3)%4] #Add losing score to an existing one
		else:
			scoreboard[l[i]] = [l[i+1], l[(i+3)%4]] #Add winning score

print('{:14} {:5} {:5}'.format('Team name', 'Won', 'Lost'))
print('-'*26)
for team in scoreboard:
	print('{:14} {:5} {:5}'.format(team, scoreboard[team][0], scoreboard[team][1]))
print('-'*26)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter game scores(format: team1 score1 - team2 score2):
When done entering, type '#' and press 'Enter'
>> Brazil 23 - America 18
>> Antarctica 18 - brazil 17
>> England 15 - Korea 19
>> africa 20 - brazil 19
>> nigeria 15 - africa 23
>> #
Team name      Won   Lost
--------------------------
brazil            59    56
america           18    23
antarctica        18    17
england           15    19
korea             19    15
africa            43    34
nigeria           15    23
--------------------------
********************************************************************************
"""