# Chapter 07: Lists

---
[bhch07exrc01.py](bhch07exrc01.py): Write a program that asks the user to enter a list of integers. Do the following:  
(a) Print the total number of items in the list.  
(b) Print the last item in the list.  
(c) Print the list in reverse order.  
(d) Print *Yes* if the list contains a 5 and *No* otherwise.  
(e) Print the number of fives in the list.  
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.  
(g) Print how many integers in the list are less than 5.  

---
[bhch07exrc02.py](bhch07exrc02.py): Write a program that generates a list of 20 random numbers between 1 and 100.  
(a) Print the list.  
(b) Print the average of the elements in the list.  
(c) Print the largest and smallest values in the list.  
(d) Print the second largest and second smallest entries in the list  
(e) Print how many even numbers are in the list.  

---
[bhch07exrc03.py](bhch07exrc03.py): Start with the list [8,9,10]. Do the following:  
(a) Set the second entry (index 1) to 17  
(b) Add 4, 5, and 6 to the end of the list  
(c) Remove the first entry from the list  
(d) Sort the list  
(e) Double the list  
(f) Insert 25 at index 3  
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]  

---
[bhch07exrc04.py](bhch07exrc04.py): Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.  

---
[bhch07exrc05.py](bhch07exrc05.py): Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.  

---
[bhch07exrc06.py](bhch07exrc06.py): Create the following lists using a for loop.  
(a) A list consisting of the integers 0 through 49  
(b) A list containing the squares of the integers 1 through 50.  
(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.  

---
[bhch07exrc07.py](bhch07exrc07.py): Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L
and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].  

---
[bhch07exrc08.py](bhch07exrc08.py): Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer.  

---
[bhch07exrc09.py](bhch07exrc09.py): When playing games where you have to roll two dice, it is nice to know the odds of each
roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
17%. You can compute these mathematically, but if you don’t know the math, you can write
a program to do it. To do this, your program should simulate rolling two dice about 10,000
times and compute and print out the percentage of rolls that come out to be 2, 3, 4, ..., 12.  

---
[bhch07exrc10.py](bhch07exrc10.py): Write a program that rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.  

---
[bhch07exrc11.py](bhch07exrc11.py): Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.  
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]  

---
[bhch07exrc12.py](bhch07exrc12.py): Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.  

---
[bhch07exrc13.py](bhch07exrc13.py): Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].  

---
[bhch07exrc14.py](bhch07exrc14.py): Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.  

---
[bhch07exrc115.py](bhch07exrc15.py): There is a provably unbreakable cipher called a one-time pad. The way it works is you shift
each character of the message by a random amount between 1 and 26 characters, wrapping
around the alphabet if necessary. For instance, if the current character is y and the shift is 5,
then the new character is d. Each character gets its own shift, so there needs to be as many
random shifts as there are characters in the message. As an example, suppose the user enters
*secret*. The program should generate a random shift between 1 and 26 for each character.
Suppose the randomly generated shifts are 1, 3, 2, 10, 8, and 2. The encrypted message would
be *thebmv*.  
(a) Write a program that asks the user for a message and encrypts the message using the
one-time pad. First convert the string to lowercase. Any spaces and punctuation in the
string should be left unchanged. For example, *Secret!!!* becomes *thebmv!!!* using
the shifts above.  
(b) Write a program to decrypt a string encrypted as above.  
The reason it is called a one-time-pad is that the list of random shifts should only be used once.
It becomes easily breakable if the same random shifts are used for more than one message.
Moreover, it is only provably unbreakable if the random numbers are truly random, and the
numbers generated by *randint* are not truly random. For this problem, just use *randint*,
but for cryptographically safe random numbers, see Section 22.8.

---
