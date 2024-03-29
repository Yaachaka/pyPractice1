#!/bin/bash
#makefile in pyPractice1

folder1:=bhch14#Object-Oriented Programming
file1:=$(folder1)exmp01#example files.
file2:=$(folder1)exrc11#exercise files.
file3:=$(file2).py#Choose between example file and exercise file.

run1:  #run python script.
	python3 $(folder1)/$(file3)

run2:  #run python script.
	echo '@@@@ Trial:' >  temporary.txt
	python3 $(folder1)/$(file3) >> temporary.txt
	cat temporary.txt >> $(folder1)/$(file3)

mk2:#Get into the chapter folder and execute there
	cd $(folder1) && python3 $(file3)

crt1:  #Create or open python file.
	#touch $(folder1)/$(file3)
	cp template1.txt $(folder1)/$(file3)
	code $(folder1)/$(file3)
	
crt2:#Create folder and README.md file.
	mkdir $(folder1)
	touch $(folder1)/README.md
	code $(folder1)/README.md
	
glog:#git log in graph
	git log --all --oneline --graph -6