#makefile in pyPractice1

folder1:=bhch02
file1:=$(folder1)exmp05#example files
file2:=$(folder1)exrc15#exercise files
file3:=$(file2).py#Choose between example file and exercise file.

runn:  #run python script.
	python3 $(folder1)/$(file3)

crt1:  #Create or open python file.
	code $(folder1)/$(file3)