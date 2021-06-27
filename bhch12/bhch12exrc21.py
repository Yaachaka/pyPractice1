"""
bhch12exrc21.py: The file high_temperatures.txt contains the average high temperatures for each day of the year in a certain city. Each line of the file consists of the date, written in the month/day format, followed by a space and the average high temperature for that date. Find the 30-day period over which there is the biggest increase in the average high temperature.
"""
print('*'*80)

temps = [line.strip().split(' ') for line in open('high_temperatures.txt')]
temps2 = [float(i[1]) for i in temps]

ind = 0
maxi = 0
for i in range(len(temps2)-30):
	s= sum(temps2[i:i+30])
	if s > maxi:
		maxi = s
		ind = i

print('The 30-day period over which there is the biggest increase in the average high temperature:')
print('\t{:} to {:}'.format(temps[ind][0], temps[ind+30][0]))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
The 30-day period over which there is the biggest increase in the average high temperature:
        3/25 to 4/24
********************************************************************************
"""