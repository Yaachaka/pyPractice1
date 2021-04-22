"""
bhch06exrc17.py:
Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
> abcdefghijklmnopqrstuvwxyz  
bcdefghijklmnopqrstuvwxyza  
cdefghijklmnopqrstuvwxyzab  
...  
yzabcdefghijklmnopqrstuvwx  
zabcdefghijklmnopqrstuvwxy  
"""
print('*'*80)

string = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
	print(string[i:], string[:i], sep='')

print('*'*80)

"""PROGRAM OUTPUT
********************************************************************************
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
defghijklmnopqrstuvwxyzabc
efghijklmnopqrstuvwxyzabcd
fghijklmnopqrstuvwxyzabcde
ghijklmnopqrstuvwxyzabcdef
hijklmnopqrstuvwxyzabcdefg
ijklmnopqrstuvwxyzabcdefgh
jklmnopqrstuvwxyzabcdefghi
klmnopqrstuvwxyzabcdefghij
lmnopqrstuvwxyzabcdefghijk
mnopqrstuvwxyzabcdefghijkl
nopqrstuvwxyzabcdefghijklm
opqrstuvwxyzabcdefghijklmn
pqrstuvwxyzabcdefghijklmno
qrstuvwxyzabcdefghijklmnop
rstuvwxyzabcdefghijklmnopq
stuvwxyzabcdefghijklmnopqr
tuvwxyzabcdefghijklmnopqrs
uvwxyzabcdefghijklmnopqrst
vwxyzabcdefghijklmnopqrstu
wxyzabcdefghijklmnopqrstuv
xyzabcdefghijklmnopqrstuvw
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy
********************************************************************************

"""