#!/usr/bin/python3
import os
import subprocess


from gtts import gTTS

f=open("helo.txt",'w')
x=" "
comm=[]
while x != "exit" :
 st=input("enter a command")
 comm.append(st)
 ts = st+";echo $?;"
 t1=[]
 t1= subprocess.getoutput(ts)
 t=t1[-1]
 if t=="0":
     f.writelines(st+"\n")
     print("command is right and is stored in file")
  
 else : 
     f.writelines(st+"\n")
     print("command is wrong and is stored in file")
 
 if len(comm) !=1:
  for i in range(0,len(comm)-1) :
   if comm[i] == st :
    tts = gTTS(text="Never run the same command", lang='en')			  
    tts.save("comd.mp3")
    os.system("xdg-open comd.mp3 ")



 

 x=input("press exit to get exit")
f.close()

