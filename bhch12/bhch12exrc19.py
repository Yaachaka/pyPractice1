"""
bhch12exrc19.py: Write a program that asks the user for a word and finds all the smaller words that can be made from the letters of that word. The number of occurrences of a letter in a smaller word can’t exceed the number of occurrences of the letter in the user’s word.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]
user_word = input('Enter a word: ').lower()

print('Possible small words:')
for word in all_words:
	if len(word) < len(user_word):
		for i in word:
			if not (i in user_word and word.count(i) <= user_word.count(i)):
				break
		else:
			print(word, ',', end='')
print()

print('*'*80)
"""PROGRAM OUTPUT
@@@@ Trial1:
********************************************************************************
Enter a word: Mohabbat
Possible small words:
a ,aa ,ab ,ah ,am ,at ,ata ,atm ,atom ,b ,ba ,bat ,bath ,bb ,bm ,bo ,boat ,bob ,bomb ,both ,bt ,h ,ha ,ham ,hat ,hb ,ho ,hot ,ht ,m ,ma ,mat ,math ,mb ,mba ,mh ,mo ,mt ,o ,ob ,oh ,om ,omaha ,ot ,t ,ta ,tab ,tb ,tba
,th ,tm ,to ,tom ,
********************************************************************************

@@@@ Trial2:
********************************************************************************
Enter a word: letters
Possible small words:
e ,ee ,el ,else ,er ,es ,est ,et ,l ,le ,lee ,les ,let ,lets ,letter ,ls ,lt ,r ,re ,reel ,rel ,res ,reset ,rest ,rl ,rs ,rt ,s ,se ,see ,ser ,set ,settle ,sl ,sr ,st ,ste ,steel ,str ,street ,t ,te ,tee ,tel ,test
,tr ,tree ,trees ,ts ,tt ,
********************************************************************************
"""