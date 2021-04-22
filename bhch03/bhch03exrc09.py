hour = eval(input('Enter hour [1 and 12]: '))
fHour = eval(input('How many hours ahead?: '))

print((hour+fHour)%12, 'o clock')