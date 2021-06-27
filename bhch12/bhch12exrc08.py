"""
bhch12exrc08.py: For this problem, use the file of NCAA basketball scores as described in Section 12.3.
(a) Find the average of the points scored over all the games in the file.
(b) Pick your favorite team and scan through the file to determine how many games they won and how many games they lost.
(c) Find the team(s) that lost by 30 or more points the most times
(d) Find all the teams that averaged at least 70 points a game.
(e) Find all the teams that had winning records but were collectively outscored by their opponents. A team is collectively outscored by their opponents if the total number of points the team scored over all their games is less than the total number of points their opponents scored in their games against the team.
"""
print('*'*80)

from pprint import pprint

full_list = [line.strip().split(', ') for line in open('basketball.txt')]
num_games = len(full_list)
match_totals = []#Holds total scores of each match

team_table = {}
for match in full_list:
	if match[1] not in team_table:
		team_table[match[1]] = [0, 0, 0, 0]#wins, losses, total_score, match_count
	if match[3] not in team_table:
		team_table[match[3]] = [0, 0, 0, 0]#wins, losses, total_score, match_count
	#wins/losses
	if int(match[2]) > int(match[4]):
		team_table[match[1]][0] += 1#Increment team1 winning score
		team_table[match[3]][1] += 1#Increment team2 losing score
	else:
		team_table[match[1]][1] += 1#Increment team1 losing score
		team_table[match[3]][0] += 1#Increment team2 winning score
	#total scores
	team_table[match[1]][2] += int(match[2])
	team_table[match[3]][2] += int(match[4])
	#Match_count
	team_table[match[1]][3] += 1
	team_table[match[3]][3] += 1
	

print('(a) Average of the points scored over all the games in the file:')
for i in full_list:
	match_totals.append(int(i[2]) + int(i[-1]))
print('Out of {:} games the averge points scored is {:}.'.format(num_games, sum(match_totals)/num_games))

print('.'*100)
print()
print('(b) Pick your favorite team to know wins/lost:')
team_name = list(team_table)
print('|{:6}|{:20}||{:6}|{:20}||{:6}|{:20}|'.format('Choice', 'Team Name', 'Choice', 'Team Name', 'Choice', 'Team Name'))
print('-'*100)
team_len = len(team_name)
for i in range(0, team_len, 3):
	print('|{:6}|{:20}|'.format(i, team_name[i]), end='')
	if i+1 < team_len:
		print('|{:6}|{:20}|'.format(i+1, team_name[i+1]), end='')
		if i+2 < team_len:
			print('|{:6}|{:20}|'.format(i+2, team_name[i+2]), end='')
	print()
print('-'*100)

choice  = eval(input('Choice: '))%team_len
print('\tTeam name: {:}'.format(team_name[choice]))
print('\tTeam wins: {:}'.format(team_table[team_name[choice]][0]))
print('\tTeam losses: {:}'.format(team_table[team_name[choice]][1]))
print('.'*100)
print()

team_30 = {}
print('(c) The team(s) that lost by 30 or more points the most times')
for match in full_list:
	score1 = int(match[2])
	score2 = int(match[4])
	if abs(score1 - score2) > 29:
		if score1 < score2:
			if match[1] not in team_30:
				team_30[match[1]] = 0
			team_30[match[1]] += 1
		else:
			if match[3] not in team_30:
				team_30[match[3]] = 0
			team_30[match[3]] += 1

if len(team_30):
	print('|{:20}|{:6}|'.format('Team name', 'Times'))
	print('-'*100)
	for team in team_30:
		print('|{:20}|{:6}|'.format(team, team_30[team]))
	print('-'*100)
else:
	print('Score difference in each match is less than 30.')

print('.'*100)
print()

print('(d) The teams that averaged at least 70 points a game:')

for team in team_table:
	if int(team_table[team][2])/int(team_table[team][3]) > 69:
		print('- {:20} (Total score of {:} in {:} matches.)'.format(team, team_table[team][2], team_table[team][3]))

print('.'*100)
print()

print('(e) The teams that had winning records of atleast 3 matches but were collectively outscored by their opponents:')
for team in team_table:
	if team_table[team][0] > 2:
		for match in full_list:
			if team in match:
				ind = 3
				if match.index(team) == 3:
					ind = 1
				if team_table[team][2] < team_table[match[ind]][2]:#Oponent with more total score
					print('- {:} with total score {:}, while {:} with total score {:}.'.format(team, team_table[team][2], match[ind], team_table[match[ind]][2]))

print('.'*100)
print()

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
(a) Average of the points scored over all the games in the file:
Out of 64 games the averge points scored is 137.375.
....................................................................................................

(b) Pick your favorite team to know wins/lost:
|Choice|Team Name           ||Choice|Team Name           ||Choice|Team Name           |
----------------------------------------------------------------------------------------------------
|     0|Arkansas-Pine Bluff ||     1|Winthrop            ||     2|Kentucky            |
|     3|East Tennessee State||     4|West Virginia       ||     5|Morgan State        |
|     6|New Mexico          ||     7|Montana             ||     8|Wisconsin           |
|     9|Wofford             ||    10|Cornell             ||    11|Temple              |
|    12|Washington          ||    13|Marquette           ||    14|Missouri            |
|    15|Clemson             ||    16|Wake Forest         ||    17|Texas               |
|    18|Syracuse            ||    19|Vermont             ||    20|Kansas State        |
|    21|North Texas         ||    22|Pittsburgh          ||    23|Oakland             |
|    24|Murray State        ||    25|Vanderbilt          ||    26|Butler              |
|    27|UTEP                ||    28|Xavier              ||    29|Minnesota           |
|    30|BYU                 ||    31|Florida             ||    32|Gonzaga             |
|    33|Florida State       ||    34|Duke                ||    35|Villanova           |
|    36|Robert Morris       ||    37|Baylor              ||    38|Sam Houston State   |
|    39|Purdue              ||    40|Siena               ||    41|Texas A&M           |
|    42|Utah State          ||    43|Old Dominion        ||    44|Notre Dame          |
|    45|Saint Mary's        ||    46|Richmond            ||    47|California          |
|    48|Louisville          ||    49|Kansas              ||    50|Lehigh              |
|    51|Ohio State          ||    52|UC Santa Barbara    ||    53|Ohio                |
|    54|Georgetown          ||    55|Maryland            ||    56|Houston             |
|    57|Michigan State      ||    58|New Mexico State    ||    59|Tennessee           |
|    60|San Diego State     ||    61|Georgia Tech        ||    62|Oklahoma State      |
|    63|Northern Iowa       ||    64|UNLV                |
----------------------------------------------------------------------------------------------------
Choice: 56
        Team name: Houston
        Team wins: 0
        Team losses: 1
....................................................................................................

(c) The team(s) that lost by 30 or more points the most times
|Team name           |Times |
----------------------------------------------------------------------------------------------------
|Wake Forest         |     1|
----------------------------------------------------------------------------------------------------
....................................................................................................

(d) The teams that averaged at least 70 points a game:
- Kentucky             (Total score of 318 in 4 matches.)
- East Tennessee State (Total score of 71 in 1 matches.)
- Cornell              (Total score of 210 in 3 matches.)
- Washington           (Total score of 218 in 3 matches.)
- Marquette            (Total score of 78 in 1 matches.)
- Missouri             (Total score of 145 in 2 matches.)
- Clemson              (Total score of 78 in 1 matches.)
- Wake Forest          (Total score of 141 in 2 matches.)
- Texas                (Total score of 80 in 1 matches.)
- Syracuse             (Total score of 225 in 3 matches.)
- Kansas State         (Total score of 323 in 4 matches.)
- Pittsburgh           (Total score of 157 in 2 matches.)
- Xavier               (Total score of 232 in 3 matches.)
- BYU                  (Total score of 171 in 2 matches.)
- Florida              (Total score of 92 in 1 matches.)
- Duke                 (Total score of 428 in 6 matches.)
- Villanova            (Total score of 141 in 2 matches.)
- Robert Morris        (Total score of 70 in 1 matches.)
- Baylor               (Total score of 287 in 4 matches.)
- Richmond             (Total score of 71 in 1 matches.)
- Kansas               (Total score of 157 in 2 matches.)
- Lehigh               (Total score of 74 in 1 matches.)
- Ohio State           (Total score of 216 in 3 matches.)
- Ohio                 (Total score of 165 in 2 matches.)
- Georgetown           (Total score of 84 in 1 matches.)
- Maryland             (Total score of 172 in 2 matches.)
- Houston              (Total score of 77 in 1 matches.)
- Tennessee            (Total score of 290 in 4 matches.)
....................................................................................................

(e) The teams that had winning records of atleast 3 matches but were collectively outscored by their opponents:
- Kentucky with total score 318, while West Virginia with total score 344.
- West Virginia with total score 344, while Duke with total score 428.
- Kansas State with total score 323, while Butler with total score 368.
- Butler with total score 368, while Duke with total score 428.
- Baylor with total score 287, while Duke with total score 428.
- Michigan State with total score 334, while Butler with total score 368.
- Tennessee with total score 290, while Michigan State with total score 334.
....................................................................................................

********************************************************************************
"""