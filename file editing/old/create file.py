import os

os.chdir("../1")
print("helloworld2 created!")
enter = input("Press ENTER to continue")

f= open("helloworld2.txt","w+")
f.write("Hello World" % (i+1))

f.close()

