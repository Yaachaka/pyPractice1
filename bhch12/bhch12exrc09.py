"""
bhch12exrc09.py: Benford’s law states that in real data where the values are spread across several orders of magnitude, about 30% of the values will start with the number 1, whereas only about 4.6% of the values will start with the number 9. This is contrary to what we might expect, namely that values starting with 1 and 9 would be equally likely. Using the file expenses.txt which consists of a number of costs from an expense account, determine what percentage start with each of the digits 1 through 9. This technique is used by accountants to detect fraud.
"""
print('*'*80)

costs = [line.strip() for line in open('expenses.txt')]
cost_len = len(costs)
digit = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

for i in costs:
	digit[i[0]] += 1

print('Percentage of values that appeared with each digit is as folows:')
print('-'*30)
print('{:5} {:10}'.format('Digit', 'Percentage'))
print('-'*30)
for i in digit:
	print('{:^5} {:9}%'.format(i, digit[i]*100/cost_len))
print('-'*30)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Percentage of values that appeared with each digit is as folows:
------------------------------
Digit Percentage
------------------------------
  1        11.6%
  2         9.5%
  3        10.9%
  4        11.3%
  5        11.4%
  6        12.7%
  7        11.0%
  8        10.9%
  9        10.7%
------------------------------
********************************************************************************
"""