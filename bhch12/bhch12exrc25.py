"""
bhch12exrc25.py: The word part has the interesting property that if you remove its letters one by one, each resulting step is a real word. For instance, part->pat->pa->a. You may remove the letters in any order, and the last (single-letter) word needs to be a real word as well. Find all eight-letter words with this property.
"""
print('*'*80)

all_words = [line.strip().lower() for line in open('wordlist.txt')]

t_words = []

for word in all_words:
	l = len(word)
	if l == 8:
		t_words.append([word])
		for i1 in range(l):
			w2 = list(word)
			del w2[i1]
			w2 = ''.join(w2)
			if w2 in all_words:
				t_words[-1].append(w2)
				for i2 in range(l-1):
					w3 = list(w2)
					del w3[i2]
					w3 = ''.join(w3)
					if w3 in all_words:
						t_words[-1].append(w3)
						for i3 in range(l-2):
							w4 = list(w3)
							del w4[i3]
							w4 = ''.join(w4)
							if w4 in all_words:
								t_words[-1].append(w4)
								for i4 in range(l-3):
									w5 = list(w4)
									del w5[i4]
									w5 = ''.join(w5)
									if w5 in all_words:
										t_words[-1].append(w5)
										for i5 in range(l-4):
											w6 = list(w5)
											del w6[i5]
											w6 = ''.join(w6)
											if w6 in all_words:
												t_words[-1].append(w6)
												for i6 in range(l-5):
													w7 = list(w6)
													del w7[i6]
													w7 = ''.join(w7)
													if w7 in all_words:
														t_words[-1].append(w7)
														for i7 in range(l-6):
															w8 = list(w7)
															del w8[i7]
															w8 = ''.join(w8)
															if w8 in all_words:
																t_words[-1].append(w8)

for i in range(len(t_words)-1, -1, -1):
	if len(t_words[i]) < 8:
		del t_words[i]

for i in t_words:
	print(i)

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
['theaters', 'theater', 'heater', 'hater', 'hate', 'ate', 'te', 'e', 't', 'ae', 'e', 'a', 'at', 't', 'a', 'hat', 'at', 't', 'a', 'ht', 't', 'h', 'ha', 'a', 'h']
********************************************************************************
"""