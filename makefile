#makefile in pyPractice1

folder1:=bhch05
file1:=$(folder1)exmp01#example files
file2:=$(folder1)exrc14#exercise files
file3:=$(file2).py#Choose between example file and exercise file.

runn:  #run python script.
	python3 $(folder1)/$(file3)

crt1:  #Create or open python file.
	code $(folder1)/$(file3)

crt2:#Create folder and README.md file.
	mkdir $(folder1)
	code $(folder1)/README.md
	
glog:#git log in graph
	git log --all --oneline --graph -6