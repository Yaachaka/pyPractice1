"""
bhch12exrc20.py: (a) Write a program that reads a file consisting of email addresses, each on its own line. Your program should print out a string consisting of those email addresses separated by semicolons.
(b) Write the same program as above, but the new string should contain only those email addresses that do not end in @prof.college.edu.
"""
print('*'*80)

from random import randint

names = [line.strip().lower() for line in open('emaillist.txt')]

part_a = ''
part_b = ''
for n in names:
	part_a += n + '; '
	i = n.index('@')
	if n[i+1:i+5] != 'prof':
		part_b += n + '; '

print('Part (a):')
print(part_a)
print('Part (b):')
print(part_b)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Part (a):
aabharana@stud.college.edu; aadeshwar@prof.college.edu; aagar@stud.college.edu; aagarna@stud.college.edu; aashirya@prof.college.edu; aasin@prof.college.edu; aavi@prof.college.edu; abezag@stud.college.edu; akalapathi@stud.college.edu; akalendra@stud.college.edu; akalesvara@prof.college.edu; akanda@prof.college.edu; akarya@prof.college.edu; gandhika@prof.college.edu; natkunam@prof.college.edu; prakruthi@stud.college.edu; pranaam@prof.college.edu; prasiddhi@prof.college.edu; pratapavat@stud.college.edu; prathish@stud.college.edu; praver@stud.college.edu; prinit@prof.college.edu; pudhumai@stud.college.edu; pujesh@stud.college.edu; puli@prof.college.edu; purnayan@prof.college.edu; purvanshu@stud.college.edu; purvith@stud.college.edu; rhyah@prof.college.edu; ruchiparv@stud.college.edu; rudhir@prof.college.edu; rupalekha@prof.college.edu; rupamanjari@stud.college.edu; rupina@stud.college.edu; rushik@prof.college.edu; rushikulya@stud.college.edu; rusyendra@stud.college.edu; rutanshi@stud.college.edu; ruthvik@stud.college.edu; ruthvika@stud.college.edu; rutwaak@stud.college.edu; suvrita@stud.college.edu; suvyuha@prof.college.edu; suyashas@prof.college.edu; svaramaya@stud.college.edu; svojas@prof.college.edu; swabhiram@stud.college.edu; swabhu@stud.college.edu; swapnasundari@stud.college.edu; swapnika@prof.college.edu; swardhuni@stud.college.edu; swarnalata@stud.college.edu; swarnalaxmi@stud.college.edu; swarnamala@prof.college.edu; swarnaprabha@prof.college.edu; swetambari@stud.college.edu; swrnav@prof.college.edu; taamraparnee@prof.college.edu; thrishika@stud.college.edu; thrithika@prof.college.edu; tisya@prof.college.edu; tivri@stud.college.edu; tokini@prof.college.edu; trinesha@prof.college.edu; turvash@stud.college.edu; turviti@stud.college.edu; tushnimsara@prof.college.edu; tushtiman@stud.college.edu; tuviksh@prof.college.edu; tuvishtam@stud.college.edu; tvashta@stud.college.edu; tvesin@prof.college.edu; udakanjali@stud.college.edu; udantika@prof.college.edu; upshobhin@stud.college.edu; urjamedh@prof.college.edu; uruthiran@stud.college.edu; usakirana@stud.college.edu; ushadevi@prof.college.edu; usharvi@prof.college.edu; ushashi@prof.college.edu; uttaragita@stud.college.edu; uttarika@prof.college.edu; vasantamalika@prof.college.edu; veeramani@stud.college.edu; vishweswari@prof.college.edu; vitaka@stud.college.edu; vividha@prof.college.edu; vivika@stud.college.edu; vivitsa@stud.college.edu; viyoginee@prof.college.edu; vridhi@stud.college.edu; vrika@prof.college.edu; vyombha@stud.college.edu; vyusta@stud.college.edu; vyusti@prof.college.edu; yaminichandra@stud.college.edu; yatharth@stud.college.edu; yatheesh@stud.college.edu; yatinatha@prof.college.edu;
Part (b):
aabharana@stud.college.edu; aagar@stud.college.edu; aagarna@stud.college.edu; abezag@stud.college.edu; akalapathi@stud.college.edu; akalendra@stud.college.edu; prakruthi@stud.college.edu; pratapavat@stud.college.edu; prathish@stud.college.edu; praver@stud.college.edu; pudhumai@stud.college.edu; pujesh@stud.college.edu; purvanshu@stud.college.edu; purvith@stud.college.edu; ruchiparv@stud.college.edu; rupamanjari@stud.college.edu; rupina@stud.college.edu; rushikulya@stud.college.edu; rusyendra@stud.college.edu; rutanshi@stud.college.edu; ruthvik@stud.college.edu; ruthvika@stud.college.edu; rutwaak@stud.college.edu; suvrita@stud.college.edu; svaramaya@stud.college.edu; swabhiram@stud.college.edu; swabhu@stud.college.edu; swapnasundari@stud.college.edu; swardhuni@stud.college.edu; swarnalata@stud.college.edu; swarnalaxmi@stud.college.edu; swetambari@stud.college.edu; thrishika@stud.college.edu; tivri@stud.college.edu; turvash@stud.college.edu; turviti@stud.college.edu; tushtiman@stud.college.edu; tuvishtam@stud.college.edu; tvashta@stud.college.edu; udakanjali@stud.college.edu; upshobhin@stud.college.edu; uruthiran@stud.college.edu; usakirana@stud.college.edu; uttaragita@stud.college.edu; veeramani@stud.college.edu; vitaka@stud.college.edu; vivika@stud.college.edu; vivitsa@stud.college.edu; vridhi@stud.college.edu; vyombha@stud.college.edu; vyusta@stud.college.edu; yaminichandra@stud.college.edu; yatharth@stud.college.edu; yatheesh@stud.college.edu;
********************************************************************************
"""