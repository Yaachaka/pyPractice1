"""
bhch08exrc09.py: Write a simple quiz game that has a list of ten questions and a list of answers to those questions. The game should give the player four randomly selected questions to answer. It should ask the questions one-by-one, and tell the player whether they got the question right or wrong. At the end it should print out how many out of four they got right.
"""
print('*'*80)

from random import randint, sample

questions = ['What is the capital of France?',
	'Which state has only one neighbor?',
	'Which is the capital of India?',
	'How many districts are there in India?',
	'Which is the national flower of India?',
	'Which is the national animal of India?',
	'Which is the national bird of India?',
	'Which is the national tree of India?',
	'Which is the smallest continent of the world?',
	'Which country holds 100%% literacy rate?'
	]

answers = ['Paris', 'Maine', 'Delhi', '732', 'Lotus', 'Tiger', 'Peacock', 'banyan', 'Australia', 'Korea Republic']

num_right = 0
randpos = sample([i for i in range(10)], 4)

for i in range(4):
	print(questions[randpos[i]])
	guess = input()

	if guess.lower()==answers[randpos[i]].lower():
		print('Correct')
		num_right=num_right+1
	else:
		print('Wrong. The answer is', answers[randpos[i]])

print('You got', num_right, 'out of 4, right.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Which is the smallest continent of the world?
Australia
Correct
Which is the national flower of India?
Lotus
Correct
What is the capital of France?
IDK
Wrong. The answer is Paris
Which is the national bird of India?
Peacock
Correct
You got 3 out of 4, right.
********************************************************************************

@@@@ Trial2:
********************************************************************************
What is the capital of France?
Forgot
Wrong. The answer is Paris
Which is the national flower of India?
Lotus
Correct
Which is the smallest continent of the world?
Australia
Correct
How many districts are there in India?
732
Correct
You got 3 out of 4, right.
********************************************************************************
"""