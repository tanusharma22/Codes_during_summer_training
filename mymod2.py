


#!/usr/bin/python3
def echotext() :
   import pyttsx3
   import datetime
   sound_var=pyttsx3.init()
   sound_var.say("enter your name")
   sound_var.runAndWait()
   sound_var.say(input())
   sound_var.runAndWait()
   currentTime = datetime.datetime.now()
   if currentTime.hour < 12:
    sound_var.say("good morning")
    sound_var.runAndWait()
   
   elif 12 <= currentTime.hour < 18:
    sound_var.say("good afternoon")
    sound_var.runAndWait()
   
   else:
    sound_var.say("good evening")
    sound_var.runAndWait()
def numbers() :
    import pyttsx3
    import os
    sound_var=pyttsx3.init()
    sound_var.say("enter how many number you want ")
    sound_var.runAndWait()
    n=int(input())
    sound_var.say("enter numbers")
    sound_var.runAndWait()
    s=[]
    for i in range(0,n) :
       l=int(input())
       s.append(l) 
    add=0 
    for i in s :
     add=add+i
    sound_var.say("addition of numbers is ")
    sound_var.runAndWait()
    sound_var.say(add)
    sound_var.runAndWait()
    sound_var.say("do you want to sort numbers")
    sound_var.runAndWait()
    t=input()
    if t=="yes" :
      sound_var.say("sorted numbers are")
      sound_var.runAndWait()       
      print(sorted(s))
    

    sound_var.say("list of installed module are")
    sound_var.runAndWait()
     
    os.system("pip3 list")
   
echotext()
numbers()
