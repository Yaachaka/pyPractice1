# Chapter 04: If Statements

---
**[bhch04exrc01.py](bhch04exrc01.py):** Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

---
**[bhch04exrc02.py](bhch04exrc02.py):** Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature
is in. Your program should convert the temperature to the other unit. The conversions
are F = (9/5)C + 32 and C = (5/9) (F - 32).  

---
**[bhch04exrc03.py](bhch04exrc03.py):** Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
- If the temperature is less than -273.15, print that the temperature is invalid because it is below absolute zero.
- If it is exactly -273.15, print that the temperature is absolute 0.
- If the temperature is between -273.15 and 0, print that the temperature is below freezing.
- If it is 0, print that the temperature is at the freezing point.
- If it is between 0 and 100, print that the temperature is in the normal range.
- If it is 100, print that the temperature is at the boiling point.
- If it is above 100, print that the temperature is above the boiling point.

---
**[bhch04exrc04.py](bhch04exrc04.py):** Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

---
**[bhch04exrc05.py](bhch04exrc05.py):** Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.

---
**[bhch04exrc06.py](bhch04exrc06.py):** A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.

---
**[bhch04exrc07.py](bhch04exrc07.py):** Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.

---
**[bhch04exrc08.py](bhch04exrc08.py):** A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.

---
**[bhch04exrc09.py](bhch04exrc09.py):** Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]

---
**[bhch04exrc10.py](bhch04exrc10.py):** Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.
> Question 1: 3 x 4 = 12  
Right!  
Question 2: 8 x 6 = 44  
Wrong. The answer is 48.  
...  
...  
Question 10: 7 x 7 = 49  
Right.  

---
**[bhch04exrc11.py](bhch04exrc11.py):** Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
> Enter hour: 8  
am (1) or pm (2)? 1  
How many hours ahead? 5  
New hour: 1 pm  

---
**[bhch04exrc12.py](bhch04exrc12.py):** A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
how much candy is in the bowl, then you win all the candy. You ask the person in charge the
following: If the candy is divided evenly among 5 people, how many pieces would be left
over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
are less than 200 pieces. Write a program to determine how many pieces are in the bowl.  

---
**[bhch04exrc13.py](bhch04exrc13.py):** Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.

---