"""
bhch12exrc22.py: In Chapter 6 there was an exercise about the game Mad Libs. It asked you to make up a story and leave out some words of the story. Your program should ask the user to enter some words and tell them what types of words to enter. Then print the full story along with the inserted words. Rewrite your program from that exercise to read the story from a file. Reading the story from a file allows people who do not know how to program to use their own stories with the program without having to change the code.
"""
print('*'*80)

name = input('Enter your name: ')
pet = input('Which is your favorite pet animal?: ')
petname = input('What do you call your pet animal?: ')

print()
file1 = open('story.txt', 'w')
print('There lived a wonderful person named, {:}.'.format(name), file=file1)
print('{:} lived happily with his friend who is a pet.'.format(name), file=file1)
print('{:} is the pet animal who was cared with a lot of love by {:}.'.format(pet, name), file = file1)
print('With love, {:} used to call his pet, {:}.'.format(name, petname), file=file1)
print('They used to play together and care for each other.', file=file1)
file1.close()

print('Your story is ready in the file \'story.txt\'.')

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Enter your name: Robert
Which is your favorite pet animal?: Horse
What do you call your pet animal?: Simon

Your story is ready in the file 'story.txt'.
********************************************************************************
"""