"""[I doubt if the notes and steps for corresponding chord types given here are right.]
bhch11exrc12.py: Below are the notes used in music:

	C C# D D# E F F# G G# A A# B

The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps past C and G is 7 steps past C. This works for any base. For example, the notes for D major are D, F#, A. We can represent the major chord steps as a list with two elements: [4, 7]. The corresponding lists for some other chord types are shown below:

Minor	        [3,7]		 Dominant seventh	 [4,7,10]
Augmented fifth	[4,8]		 Minor seventh	     [3,7,10]
Minor fifth	    [4,6]		 Major seventh	     [4,7,11]
Major sixth	    [4,7,9]		 Diminished seventh	 [3,6,10]
Minor sixth	    [3,7,9]		

Write a program that asks the user for the key and the chord type and prints out the notes of the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists of steps.
"""
print('*'*80)

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notes_len = len(notes)
chord_dict = {'major': [0,4,7], 'minor': [0, 3, 7], 'augmented fifth': [0, 4, 8], 'minor fifth': [0, 4, 6], 'major sixth': [0, 4, 7, 9], 'minor sixth': [0, 3, 7, 9], 'dominant seventh': [0, 4, 7, 10], 'minor seventh': [0, 3, 7, 10], 'major seventh': [0, 4, 7, 11], 'diminished seventh': [0, 3, 6, 10]}
chords = list(chord_dict)

#Getting user input
key = input('Choose your musical key (options: {:}): '.format(notes)).upper()
if key in notes:#if the user eners key from available options ask for chord type and proceed.
	print('\nChoose from the available chord types.')
	print('{:20}{:6}'.format('Chord type', 'Choice'))
	print('-'*30)
	for i in range(len(chords)):
		print('{:20}{:^6}'.format(chords[i], i))
	print('-'*30)
	chord_type = eval(input('Your choice: '))%len(chords)
	print('You chose \'{:} {:}\'.'.format(key, chords[chord_type]))

	print('\nThe notes are ')
	steps = chord_dict[chords[chord_type]]
	ind = notes.index(key)
	for i in range(len(steps)):
		print(notes[(ind + steps[i]) % notes_len], end = ' ')

	print()
	
else:#if the user doesn't enter right musical key
	print('Musical key you entered does not exist in our library.')


print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Choose your musical key (options: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']): a

Choose from the available chord types.
Chord type          Choice
------------------------------
major                 0
minor                 1
augmented fifth       2
minor fifth           3
major sixth           4
minor sixth           5
dominant seventh      6
minor seventh         7
major seventh         8
diminished seventh    9
------------------------------
Your choice: 8
You chose 'A major seventh'.

The notes are
A C# E G#
********************************************************************************

@@@@ Trial2:
********************************************************************************
Choose your musical key (options: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']): c

Choose from the available chord types.
Chord type          Choice
------------------------------
major                 0
minor                 1
augmented fifth       2
minor fifth           3
major sixth           4
minor sixth           5
dominant seventh      6
minor seventh         7
major seventh         8
diminished seventh    9
------------------------------
Your choice: 0
You chose 'C major'.

The notes are
C E G
********************************************************************************
"""