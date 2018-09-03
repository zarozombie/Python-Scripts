#need to work on file

import os



dir = input ("what directory do you want to search in?\n")

#os.chdir("./1")
os.chdir(dir)

def header():
	print('                               Files in Dir             ')
	print('--------------------------------------------------------------------------')
	print('\n')
	
def footer():
	print('\n')
	print('--------------------------------------------------------------------------')
	print('\n')
	pause = input("                      PRESS ENTER TO Close.")

header()
for root, dirs, files in os.walk("."):  
    for filename in files:

        print(filename)
		
footer()