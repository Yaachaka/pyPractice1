temperature = eval(input('Enter a temperature: '))
unit = eval(input('Enter unit of temperature(1 for Celsius and 2 for Fahrenheit): '))

if unit == 1:
	print('Temperature in Fahrenheit: ', 9 * temperature / 5 + 32)
elif unit == 2:
	print('Temperature in Celsius: ', (5/9)*(temperature - 32))
else:
	print('Inavlid unit of temperature.')