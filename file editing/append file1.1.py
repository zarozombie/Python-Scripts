import os

os.chdir("./1")

for root, dirs, files in os.walk("."):  
	for filename in files:
		print(filename)
		
file = input("\nWhat file do you want to append?\n")
string = input("enter text\n")

with open(file, 'a') as the_file:
	the_file.write('\n')
	the_file.write(string)
	
update = input("File updated!\nPress ENTER to continue")	
	