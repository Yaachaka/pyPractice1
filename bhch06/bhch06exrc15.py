"""
bhch06exrc15.py):**  
When I was a kid, we used to play this game called *Mad Libs*. The way it worked was a friend
would ask me for some words and then insert those words into a story at specific places
and read the story. The story would often turn out to be pretty funny with the words I had
given since I had no idea what the story was about. The words were usually from a specific
category, like a place, an animal, etc.
For this problem you will write a *Mad Libs* program. First, you should make up a story and
leave out some words of the story. Your program should ask the user to enter some words
and tell them what types of words to enter. Then print the full story along with the inserted
words. Here is a small example, but you should use your own (longer) example:
	Enter a college class: CALCULUS  
	Enter an adjective: HAPPY  
	Enter an activity: PLAY BASKETBALL  
	CALCULUS class was really HAPPY today. We learned how to
	PLAY BASKETBALL today in class. I can't wait for tomorrow's
	class!
"""
print('*'*80)

name = input('Enter your name: ')
pet = input('Which is your favorite pet animal?: ')
petname = input('What do you call your pet animal?: ')

print()
print('There lived a wonderful person named, ', name, '.', sep='')
print(name, 'lived happily with his friend who is a pet.')
print(pet, ' is the pet animal who was cared with a lot of love by ', name, '.', sep='')
print('With love, ', name, ' used to call his pet, ', petname, '.', sep='')
print('They used to play together and care for each other.')

print('*'*80)
"""PROGRAM OUTPUT

Trial1:
********************************************************************************
Enter your name: Dharma
Which is your favorite pet animal?: Horse
What do you call your pet animal?: Bhaadshah

There lived a wonderful person named, Dharma.
Dharma lived happily with his friend who is a pet.
Horse is the pet animal who was cared with a lot of love by Dharma.
With love, Dharma used to call his pet, Bhaadshah.
They used to play together and care for each other.
********************************************************************************
"""