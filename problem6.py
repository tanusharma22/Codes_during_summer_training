#!/usr/bin/python3
import sys

string=input("enter your cat command to show content and catap to append")
list=string.split()
t=list
if t[0]=='cat':
 if t[1]=='>' :
  f=open(t[2],'w')
  f.write(input("enter your content"))
  f.close()

 else :
  f = open(t[1], "r")
  print(f.readlines())
  f.close()

elif t[0]=='catap':
  f=open(t[1], "r")
  s=f.readlines()
  f.close()
  
  f=open(t[3], "a")
  f.writelines(s)
  f.close()  

'''#adding content to file

fo = open("hello.txt", "a+")
fo.write("tanuhgchvhgvjhvjhgjhbjhbjhb")

print(fo.read())

fo.close()
'''
