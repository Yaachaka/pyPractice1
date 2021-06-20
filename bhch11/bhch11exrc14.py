"""
bhch11exrc14.py: Dictionaries provide a convenient way to store structured data. Here is an example dictionary:

	d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
	{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
	{'name':'Princess', 'phone':'555-3141', 'email':''},
	{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

Write a program that reads through any dictionary like this and prints the following:
(a) All the users whose phone number ends in an 8
(b) All the users that don’t have an email address listed
"""
print('*'*80)

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'},
{'name':'John', 'phone':'555-1817', 'email':'john@mail.net'},
{'name':'Galga', 'phone':'555-1618', 'email':''},
{'name':'Prince', 'phone':'555-5691', 'email':''},
{'name':'DJ', 'phone':'555-3758', 'email':'dj@mail.net'}]

print('(a) All the users whose phone number ends in an 8:')
print('{:12}{:8}   {:22}'.format('Name', 'Phone', 'E-mail'))
print('-'*50)
for i in d:
	if i['phone'][-1] == '8':
		print('{:12}{:8}   {:22}'.format(i['name'], i['phone'], i['email']))
print('-'*50)

print('\n(b) All the users that don’t have an email address listed:')
print('{:12}{:8}'.format('Name', 'Phone'))
print('-'*25)
for i in d:
	if len(i['email']) == 0:
		print('{:12}{:8}'.format(i['name'], i['phone']))
print('-'*25)


print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
(a) All the users whose phone number ends in an 8:
Name        Phone      E-mail                
--------------------------------------------------
Helga       555-1618   helga@mail.net        
LJ          555-2718   lj@mail.net           
Galga       555-1618                         
DJ          555-3758   dj@mail.net           
--------------------------------------------------

(b) All the users that don’t have an email address listed:
Name        Phone   
-------------------------
Princess    555-3141
Galga       555-1618
Prince      555-5691
-------------------------
********************************************************************************
"""