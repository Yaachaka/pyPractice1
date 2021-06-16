"""
bhch10exrc08.py: Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in a 6.
"""
print('*'*80)

l1 = [i for i in range(1, 1001) if i % 10 == 6 and not i % 7]
print(l1)

print('*'*80)
"""PROGRAM OUTPUT

@@@@ Trial1:
********************************************************************************
[56, 126, 196, 266, 336, 406, 476, 546, 616, 686, 756, 826, 896, 966]
********************************************************************************
"""