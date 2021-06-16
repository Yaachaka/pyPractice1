"""
bhch10exrc32.py: Monte Carlo simulations can be used to estimate all sorts of things, including probabilities of coin flip and dice events. As an example, to estimate the probability of rolling a pair of sixes with two dice, we could use random integers to simulate the dice and run the simulation thousands of times, counting what percentage of the time a pair of sixes comes up.
(a) Estimate the probability of rolling a Yahtzee in a single roll of five dice. That is estimate the probability that when rolling five dice they all come out to be the same number.
(b) Estimate the probability of rolling a large straight in a single roll of five dice. A large straight is a roll where the dice come out 1-2-3-4-5 or 2-3-4-5-6 in any order.
(c) Estimate the average longest run of heads or tails when flipping a coin 200 times.
(d) Estimate the average number of coin flips it takes before five heads in a row come up.
(e) Estimate the average number of coin flips it takes before the string s comes up, where s is a string of heads and tails, like HHTTH.
"""
print('*'*80)

from random import randint

print('(a) Estimate the probability of rolling a Yahtzee in a single roll of five dice. That is estimate the probability that when rolling five dice they all come out to be the same number.')
dices = [0 for i in range(5)]
count = 10000
times = 0
large_straight = 0
for i in range(count):
	for j in range(5):
		dices[j] = randint(1, 6)
	if dices.count(dices[0]) == 5:
		times += 1
	dices.sort()
	if dices == list(range(1, 6)) or dices == list(range(2, 7)):
		large_straight += 1

print('Probability of rolling same number on all dices on {:} rolls is {:}.\n'.format(count, times))

print('(b) Estimate the probability of rolling a large straight in a single roll of five dice. A large straight is a roll where the dice come out 1-2-3-4-5 or 2-3-4-5-6 in any order.')
print('Probability of rolling large straight on {:} rolls is {:}.\n'.format(count, large_straight))

print('(c) Estimate the average longest run of heads or tails when flipping a coin 200 times.')
count = 200
sides = ['H', 'T']
flips = []
times = 0
flip2 = ''
s = "HHTTH" #We may change this string to check if it exists
for i in range(count):
	g = randint(0, 1)
	if not g:
		times += 1
	else:
		flips.append(times)
		times = 0
	flip2 += sides[g]

print(flips)
avg = sum(flips)/len(flips)
print('Average longest run of heads on {:} flips is {:.4f}.\n'.format(count, avg))

print('(d) Estimate the average number of coin flips it takes before five heads in a row come up.')
if flips.count(5):
	print('It took {:} flips before five heads in a row appeared.\n'.format(flips.index(5)))
else:
	print('Five heads in a row did not occur.')

print('(e) Estimate the average number of coin flips it takes before the string s comes up, where s is a string of heads and tails, like HHTTH.')
length = len(s)
if s in flip2:
	print('The no. of flips it took before the string appeared is {:}.'.format(flip2.index(s)))
else:
	print('The string hasn\'t occured.')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
(a) Estimate the probability of rolling a Yahtzee in a single roll of five dice. That is estimate the probability that when rolling five dice they all come out to be the same number.
Probability of rolling same number on all dices on 10000 rolls is 10.

(b) Estimate the probability of rolling a large straight in a single roll of five dice. A large straight is a roll where the dice come out 1-2-3-4-5 or 2-3-4-5-6 in any order.
Probability of rolling large straight on 10000 rolls is 326.

(c) Estimate the average longest run of heads or tails when flipping a coin 200 times.
[3, 0, 2, 4, 1, 0, 2, 0, 2, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 3, 0, 1, 1, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 2, 0, 1, 2, 1, 0, 0, 4, 0, 2, 0, 0, 1, 2, 1, 1, 0, 5, 1, 0, 0, 2, 2, 1, 1, 1, 1, 3, 1, 0, 1, 0, 1, 2, 1, 0, 3, 2, 1, 0, 2, 1, 0, 1, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 7]
Average longest run of heads on 200 flips is 0.9700.

(d) Estimate the average number of coin flips it takes before five heads in a row come up.
It took 56 flips before five heads in a row appeared.

(e) Estimate the average number of coin flips it takes before the string s comes up, where s is a string of heads and tails, like HHTTH.
The no. of flips it took before the string appeared is 1.
********************************************************************************

@@@@ Trial2:
********************************************************************************
(a) Estimate the probability of rolling a Yahtzee in a single roll of five dice. That is estimate the probability that when rolling five dice they all come out to be the same number.
Probability of rolling same number on all dices on 10000 rolls is 8.

(b) Estimate the probability of rolling a large straight in a single roll of five dice. A large straight is a roll where the dice come out 1-2-3-4-5 or 2-3-4-5-6 in any order.
Probability of rolling large straight on 10000 rolls is 326.

(c) Estimate the average longest run of heads or tails when flipping a coin 200 times.
[0, 0, 3, 1, 1, 0, 0, 1, 6, 4, 1, 0, 0, 1, 1, 4, 3, 1, 0, 0, 1, 3, 0, 2, 6, 1, 3, 3, 4, 1, 0, 0, 0, 0, 0, 2, 5, 1, 0, 0, 0, 0, 5, 1, 1, 0, 6, 4, 0, 4, 1, 0, 5, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 3]
Average longest run of heads on 200 flips is 1.1630.

(d) Estimate the average number of coin flips it takes before five heads in a row come up.
It took 36 flips before five heads in a row appeared.

(e) Estimate the average number of coin flips it takes before the string s comes up, where s is a string of heads and tails, like HHTTH.
The no. of flips it took before the string appeared is 50.
********************************************************************************
"""