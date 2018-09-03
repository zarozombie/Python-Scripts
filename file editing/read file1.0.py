import os

os.chdir("./1")

for root, dirs, files in os.walk("./Bible"):  
	for filename in files:
		print(filename)

option = input("\nwhat file do you want to read?\n")
# number = option
name = option

def header():
	print('                               File             ')
	print('--------------------------------------------------------------------------')
	print('\n')
	
def footer():
	print('--------------------------------------------------------------------------')
	print('\n')
	wait2 = input("                      PRESS ENTER TO Close.")

# try:
file_name = os.path.isfile(name)
# print (file_name)
# pause = input()

if (file_name == True):
	print ('this is true')

	header()

	f = open(name,'r')
	print(f.read())
	footer()

	pause = input('press ENTER')

else:
	print ('this file does not exist')
	pause = input('press ENTER')
