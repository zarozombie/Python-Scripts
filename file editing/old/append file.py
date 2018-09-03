import os

os.chdir("../1")

with open('helloworld2.txt', 'a') as the_file:
    the_file.write('\nHello\n')
	
wait3 = input("file updated")	
	