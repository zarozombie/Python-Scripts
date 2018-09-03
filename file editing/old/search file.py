#need to work on file

import os

os.chdir("../1")

#from os import listdir
#from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#print (onlyfiles)


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