"""
bhch10exrc30.py: Pascal’s triangle is shown below. On the outside are 1’s and each other number is the sum of the two numbers directly above it. Write a program to generate Pascal’s triangle. Allow the user to specify the number of rows. Be sure that it is nicely formatted, like below.
           1
        1     1
      1    2    1
    1   3     3   1
  1   4    6    4   1
1   5   10   10   5   1
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""
print('*'*80)

rows = eval(input('Enter number of rows to print: '))
#Generating Pascal's triangle's values
l1 = [[1], [1, 1]]
for i in range(2, rows):
	l1.append([1]*(i+1))
	for j in range(1,i):
		l1[i][j] = l1[i-1][j-1] + l1[i-1][j]
		
#Printing Pascal's triangle
space = len(str(max(l1[rows-1])))
for i in range(rows):
	print('  '*((rows-1-i)*space//2), end='')
	for j in l1[i]:
		print('{:{:}d}'.format(j, space), end= ' '*space)
	print()

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter number of rows to print: 6
           1  
         1   1  
       1   2   1  
     1   3   3   1  
   1   4   6   4   1  
 1   5  10  10   5   1  
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter number of rows to print: 10
                            1   
                          1     1   
                      1     2     1   
                    1     3     3     1   
                1     4     6     4     1   
              1     5    10    10     5     1   
          1     6    15    20    15     6     1   
        1     7    21    35    35    21     7     1   
    1     8    28    56    70    56    28     8     1   
  1     9    36    84   126   126    84    36     9     1   
********************************************************************************

@@@@ Trial:
********************************************************************************
Enter number of rows to print: 15
                                                           1    
                                                       1       1    
                                                   1       2       1    
                                               1       3       3       1    
                                           1       4       6       4       1    
                                       1       5      10      10       5       1    
                                   1       6      15      20      15       6       1    
                               1       7      21      35      35      21       7       1    
                           1       8      28      56      70      56      28       8       1    
                       1       9      36      84     126     126      84      36       9       1    
                   1      10      45     120     210     252     210     120      45      10       1    
               1      11      55     165     330     462     462     330     165      55      11       1    
           1      12      66     220     495     792     924     792     495     220      66      12       1    
       1      13      78     286     715    1287    1716    1716    1287     715     286      78      13       1    
   1      14      91     364    1001    2002    3003    3432    3003    2002    1001     364      91      14       1    
********************************************************************************
"""