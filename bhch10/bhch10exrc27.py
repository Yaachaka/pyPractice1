"""
bhch10exrc27.py: Write a program that simulates all possible rolls of four dice and for each simulated roll, finds the sums of pairs of dice. For instance, if the roll is 5 1 2 4, the sums are 6, 8, 9, 3 ,5, and 6. For each of the possible sums from 2 to 12, find the total number of simulated rolls in which the sum appears and what percentage of the simulated rolls had those sums appear. Output the totals and percentages, nicely formatted, with the percentages formatted to one decimal place. To check your work, you should find that the sum 2 comes up in 171 rolls, which is 13.2% of the rolls.
"""
print('*'*80)

from random import randint

sum_count = [0]*13
total_rolls = 500

for i in range(total_rolls):
	current_roll = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
	current_sum = [current_roll[j]+current_roll[k] for j in range(len(current_roll)-1) for k in range(j+1, len(current_roll))]
	for i in range(2, 13):
		if current_sum.count(i):
			sum_count[i] += 1

print('For total of {:} rolls,'.format(total_rolls))
print('Sum  Total   Percentage')
for i in range(2, 13):
	print('{:3d}  {:5d}   {:6.2f}%'.format(i, sum_count[i], sum_count[i]*100/total_rolls))
print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
For total of 500 rolls,
Sum  Total   Percentage
  2     73    14.60%
  3    130    26.00%
  4    188    37.60%
  5    221    44.20%
  6    271    54.20%
  7    323    64.60%
  8    276    55.20%
  9    227    45.40%
 10    167    33.40%
 11    116    23.20%
 12     64    12.80%
********************************************************************************

@@@@ Trial2:
********************************************************************************
For total of 500 rolls,
Sum  Total   Percentage
  2     70    14.00%
  3    101    20.20%
  4    170    34.00%
  5    219    43.80%
  6    277    55.40%
  7    325    65.00%
  8    274    54.80%
  9    227    45.40%
 10    189    37.80%
 11    109    21.80%
 12     82    16.40%
********************************************************************************

@@@@ Trial3:
********************************************************************************
For total of 500 rolls,
Sum  Total   Percentage
  2     65    13.00%
  3    110    22.00%
  4    185    37.00%
  5    210    42.00%
  6    279    55.80%
  7    292    58.40%
  8    265    53.00%
  9    223    44.60%
 10    171    34.20%
 11    131    26.20%
 12     73    14.60%
********************************************************************************
"""