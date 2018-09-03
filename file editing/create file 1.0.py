import os

os.chdir("./1")

filename = input("Please name file\n")
string = input("what do you want the file to say?\n")

f = open(filename,"w+")
f.write(string)	 
f.close()