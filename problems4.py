#!/usr/bin/python3
import os


string=input("Enter username:-")

data=[]
for i in string:
	data.append(i)
	if i.isalpha()==True:
		continue
	elif i.isdigit()==True:
		print("Please enter only string in username!!")
		exit()

os.system("useradd "+string)

os.system("passwd "+string)

print("a new user is created")

'''or simply use os.system("useradd -p "+password+" "+string)


