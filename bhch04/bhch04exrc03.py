temp_celsius = eval(input('Enter temperature in celsius: '))

if temp_celsius < -273.15:
	print('The temperature is invalid because it is below absolute zero.')
elif temp_celsius == -273.15:
	print('The temperature is absolute zero.')
elif -273.15 < temp_celsius < 0:
	print('The temperature is below freezing.')
elif temp_celsius == 0:
	print('The temperature is at the freezing point.')
elif 0 < temp_celsius < 100:
	print('The temperature is in the normal range.')
elif temp_celsius == 100:
	print('The temperature is at the boiling point.')
else:
	print('The temperature is above the boiling point.')