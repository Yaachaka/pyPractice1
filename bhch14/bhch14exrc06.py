"""
bhch14exrc06.py: Write a class called Converter. The user will pass a length and a unit when declaring an object from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there should be a method that returns the length converted into those units. For example, using the Converter object created above, the user could call c.feet() and should get 0.75 as the result.
"""
print('*'*80)

units = ['inches', 'feet', 'yards', 'miles', 'kilometers', 'meters', 'centimeters', 'millimeters']
unit_c = [
	[1, 0.0834, 0.0278, 1.5782e-5, 2.54e-4, 0.0254, 2.54, 25.4], #inches
	[12, 1, 0.3334, 1.8939e-4, 3.048e-4, 0.3048, 30.48, 304.8], #feet
	[36, 3, 1, 5.6818e-4, 9.144e-4, 0.9144, 91.44, 914.4], #yards
	[63360, 5280, 1760, 1, 1.609344, 1609.344, 160934.4, 1609344], #miles
	[39370.0787, 3280.8398, 1093.6132, 0.6213, 1, 1e3, 1e5, 1e6], #kilometers
	[39.3700, 3.2808, 1.0936, 6.2137e-4, 0.001, 1, 100, 1000], #meters
	[0.3937, 0.0328, 0.0109, 6.2137e-6, 1e-5, 0.01, 1, 10], #centimeters
	[0.0393, 0.0032, 0.0010, 0.6213e-6, 1e-6, 0.001, 0.1, 1], #millimeteres
]

class Converter:
	def __init__(self, length, unit):
		self.length = length
		self.unit = unit

	def process(self, i, u):
		return self.length * unit_c[i][units.index(u)]
	
	def inches(self):
		return self.process(units.index(self.unit), units[0])
	
	def feet(self):
		return self.process(units.index(self.unit), units[1])
	
	def yards(self):
		return self.process(units.index(self.unit), units[2])
	
	def miles(self):
		return self.process(units.index(self.unit), units[3])
	
	def kilometers(self):
		return self.process(units.index(self.unit), units[4])
	
	def meters(self):
		return self.process(units.index(self.unit), units[5])
	
	def centimeters(self):
		return self.process(units.index(self.unit), units[6])
	
	def millimeters(self):
		return self.process(units.index(self.unit), units[7])
	
length = eval(input('Enter length: '))
print('Choose units: ')
for i in  range(len(units)):
	print('{:} - {:}'.format(i, units[i]))
unit1_ind = eval(input('Choose current unit: '))%len(units)
unit2_ind = eval(input('Choose needed unit: '))%len(units)

l1 = Converter(length, units[unit1_ind])
k = eval('l1.' + units[unit2_ind] + '()')

print('That is equal to {} {}.'.format(k, units[unit2_ind]))
		
print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter length: 10
Choose units:
0 - inches
1 - feet
2 - yards
3 - miles
4 - kilometers
5 - meters
6 - centimeters
7 - millimeters
Choose current unit: 3
Choose needed unit: 4
That is equal to 16.09344 kilometers.
********************************************************************************
"""