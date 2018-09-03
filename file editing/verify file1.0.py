import os.path
os.chdir("./1")

search = input("What file are you looking for?")
check = os.path.isfile(search) 

if check == True:
	print ("This File is truely there" + " " + search)
	pause = input("Please press ENTER to continue")
	
else:
	print(check)
	pause = input("Please press ENTER to continue")

