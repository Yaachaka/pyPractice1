from math import floor

year = eval(input('Enter a year: '))

C = year//100
m = (15 + C - floor(C/4) - floor((8*C + 13)/25)) % 30
n = (4 + C - floor(C/4)) % 7
a = year % 4
b = year % 7
c = year % 19
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7

print('Day:', d)
print('Unfinished: Incomplete understanding.')