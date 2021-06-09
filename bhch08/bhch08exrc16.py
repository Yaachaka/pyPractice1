"""
bhch08exrc16.py: Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to produce a list of the gaps between consecutive entries in L. Then find the maximum gap size and the percentage of gaps that have size 2.
"""
print('*'*80)

l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

l2 = [l[i]-l[i-1] for i in range(1,len(l))]

print('l = ', l)
print('l2 = ', l2)
print('Maximum gap size is', max(l2))
print('Percentage of gaps that have size 2 is', round(l2.count(2)*100/len(l2), 2), '%')

print('*'*80)

"""PROGRAM OUTPUT
********************************************************************************
l =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
l2 =  [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4]
Maximum gap size is 6
Percentage of gaps that have size 2 is 42.86 %
********************************************************************************
"""