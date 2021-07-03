"""
bhch13exrc19.py: Write a function called verbose that, given an integer less than 10^15, returns the name of the integer in English. As an example, verbose(123456) should return one hundred twenty-three thousand, four hundred fifty-six.
"""
print('*'*80)

checkpoints = {'0':'', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety', '1e2':'hundred', '1e3':'thousand', '1e5':'lakh', '1e6':'million', '1e7':'crore', '1e9':'billion', '1e12':'trillion', '1e15':'quadrillion'}


#Function
def verbose(n):
	#Adjusting the recieved number
	#if n = 123456 then  slot = 0000000000123456
	max = 16
	n_len = len(str(n))
	global slot
	global value
	
	slot = '0'*max#Limited for 1e15
	slot = slot[:-n_len] + str(n)
	#16-15 in slot is quadrillion, 14-13 in slot is trillion, 12-10 in slot is billion, 9-8 in slot is crore, 7-6 in slot is lakh, 5-4 in slot is thousand, 3 in slot is hundred, 2 in slot is tens and 1 in slot is ones.
	value = []
	i = 0

	if n_len > max - i - 2:#slot of quadrillion
		f1(i)
		if slot[i] != '0' or slot[i+1] != '0':
			value.append('quadrillion')
	i += 2#i = 2
	if n_len > max - i - 2:#slot of trillion
		f1(i)
		if slot[i] != '0' or slot[i+1] != '0':
			value.append('trillion')
	i += 2#i = 4
	if n_len > max - i - 2:#slot of billion
		value.append(checkpoints[slot[i]])
		if slot[i] != '0':
			value.append('hundred')
	i += 1#i = 5
	if n_len > max - i - 2:#slot of billion
		f1(i)
		if slot[i-1] != '0' or slot[i] != '0' or slot[i+1] != '0':
			value.append('billion')
	i += 2#i = 7
	if n_len > max - i - 2:#slot of crore
		f1(i)
		if slot[i] != '0' or slot[i+1] != '0':
			value.append('crore')
	i += 2#i = 9
	if n_len > max - i - 2:#slot of lakh
		f1(i)
		if slot[i] != '0' or slot[i+1] != '0':
			value.append('lakh')
	i += 2#i = 11
	if n_len > max - i - 2:#slot of thousand
		f1(i)
		if slot[i] != '0' or slot[i+1] != '0':
			value.append('thousand')
	i += 2#i = 13
	if n_len > max - i - 2:#slot of hundred
		value.append(checkpoints[slot[i]])
		if slot[i] != '0':
			value.append('hundred')
	i += 1#i = 14
	f1(i)#2-1 in slot
	
	value = ' '.join(value)
	while '  ' in value:#Remove extra spaces
		value = value.replace('  ', ' ')
	
	return value

def f1(i):#evaluate 2-digit slots
	if slot[i] == '1':#slot of tens
		value.append(checkpoints[slot[i:i+2]])
	else:
		if slot[i] != '0':#slot of tens
			value.append(checkpoints[slot[i] + '0']) #if we have 21 then print twenty here and one from the following commands
		value.append(checkpoints[slot[i+1]])#slot of ones
	
#Program starts here
n = abs(int(eval(input('Enter an integer: '))))
if n > 0:
	if n <= 1e15:
		print(verbose(n))
	else:
		print('Can\'t evaluate this value. Value too large. Sorry :(')
if n == 0:
	print('zero')

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter an integer: 120000000000000
one quadrillion twenty trillion
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter an integer: 1200000000000000
Can't evaluate this value. Value too large. Sorry :-{(
********************************************************************************

@@@@ Trial3:
********************************************************************************
Enter an integer: 1000000000000000
ten quadrillion
********************************************************************************

@@@@ Trial4:
********************************************************************************
Enter an integer: 90000000000000
ninety trillion
********************************************************************************

@@@@ Trial5:
********************************************************************************
Enter an integer: 900000000000000
nine quadrillion
********************************************************************************

@@@@ Trial6:
********************************************************************************
Enter an integer: 909090909090
nine hundred nine billion nine crore nine lakh nine thousand ninety
********************************************************************************

@@@@ Trial7:
********************************************************************************
Enter an integer: 123112335434
one hundred twenty three billion eleven crore twenty three lakh thirty five thousand four hundred thirty four
********************************************************************************
"""