"""
bhch10exrc04.py: Write a program that takes a list of ten prices and ten products, applies an 11% discount to each of the prices displays the output like below, right-justified and nicely formatted.

Apples   $  2.45
Oranges  $ 18.02
...
Pears    $120.03
"""
print('*'*80)

from random import random

item = ['Apples', 'Oranges', 'Grapes', 'Banana', 'Onion', 'Garlic', 'Pears', 'Watermelon', 'Mango', 'Beans']
cost = [random()*999*0.89 for i in range(10)]

print('{:12s}Cost'.format('Item'))
for i in range(len(item)):
	print('{:12s}${:6.2f}'.format(item[i], cost[i]))

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Item        Cost
Apples      $851.25
Oranges     $184.49
Grapes      $301.20
Banana      $ 82.95
Onion       $383.25
Garlic      $297.63
Pears       $694.19
Watermelon  $214.92
Mango       $857.26
Beans       $605.12
********************************************************************************

@@@@ Trial2:
********************************************************************************
Item        Cost
Apples      $ 76.02
Oranges     $386.32
Grapes      $406.94
Banana      $636.70
Onion       $123.45
Garlic      $340.32
Pears       $131.09
Watermelon  $678.31
Mango       $595.07
Beans       $579.78
********************************************************************************
"""