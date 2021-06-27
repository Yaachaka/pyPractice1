"""
bhch12exrc07.py: You are given a file called baseball.txt. A typical line of the file starts like below.

	Ichiro Suzuki	SEA	162	680	74	...[more stats]

Each entry is separated by a tab, \t. The first entry is the player’s name and the second is their team. Following that are 16 statistics. Home runs are the seventh stat and stolen bases are the eleventh. Print out all the players who have at least 20 home runs and at least 20 stolen bases.
"""
print('*'*80)

file1 = [line.strip().split('\t') for line in open('baseball.txt')]

for i in file1:
	if int(i[8]) > 19 and int(i[12]):
		print('{:20}{:}'.format(i[0], ' '.join(i[1:])))

print('*'*80)
"""PROGRAM OUTPUT
********************************************************************************
Ichiro Suzuki       MBC 732 945 929 747 389 278 21 721 803 107 41 146 838 474 400 855
Chris Ronaldo       JBM 522 394 174 571 121 465 48 711 591 763 31 621 308 439 698 149
Ant Man             IZP 722 366 732 623 958 905 36 208 911 362 41 275 685 585 914 777
Iron Man            JKQ 576 659 893 380 254 989 41 131 991 356 25 759 868 254 657 986
Rocky Boy           FID 322 674 111 415 328 727 31 706 761 526 29 791 733 123 307 966
Jackie Chan         FDY 904 892 947 577 520 926 37 256 287 575 18 792 144 794 911 282
Bruce Lee           HFX 766 977 565 686 962 638 22 192 208 629 25 113 402 768 365 706
Aqua Man            VAE 220 807 954 102 154 325 20 793 728 621 47 436 743 263 543 401
Bat Man             PND 597 237 488 145 203 317 33 657 204 735 35 683 776 318 554 333
Wonder Woman        KGH 871 951 824 237 203 901 45 728 980 156 43 677 742 767 161 560
Doctor Strange      RJO 546 346 854 956 178 825 21 195 863 882 42 195 425 993 368 249
Tony Stark          NRZ 142 755 463 234 513 709 25 666 840 524 47 811 230 765 259 795
Thor Ragnarok       RJA 185 696 949 170 737 949 24 707 773 306 33 960 160 751 454 177
Steve Rogers        KME 262 900 818 251 730 971 41 666 867 303 25 405 975 920 670 109
Hugh Jackson        JDN 528 899 378 598 808 242 39 539 590 793 17 911 447 405 335 679
Black Widow         MKC 102 721 671 836 551 485 27 679 457 200 16 706 258 975 822 532
Black Panther       IDF 251 765 173 634 417 472 42 855 418 795 15 987 709 714 758 541
Nick Fury           EMY 177 195 848 442 357 264 36 715 493 523 40 708 970 893 420 860
Ms Potts            ASF 437 969 273 853 667 479 24 252 279 954 19 710 574 588 518 854
Lt Rhodey           BSJ 916 949 761 191 519 617 27 486 456 983 41 200 527 674 462 334
Sakherine           SEW 565 227 943 572 369 706 22 110 165 933 29 396 671 286 892 162
********************************************************************************
"""