#!/usr/bin/python3
from googlesearch import search
import time
web=input("enter a topic")
url=[]
for i in search(web,stop=10) :
  print(i)
  time.sleep(1)   
  url.append(i)
  print(url)
