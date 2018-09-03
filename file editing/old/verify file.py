import os.path
os.chdir("../1")

check = os.path.isfile("helloworld2.txt") 

if check == True:
	print ("This File is truely there (helloworld2.txt)")
	pause = input("Please press ENTER to continue")
	
else:
	print(check)
	pause = input("Please press ENTER to continue")

