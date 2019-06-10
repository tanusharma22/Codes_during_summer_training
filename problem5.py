#!/usr/bin/python3
import datetime
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    print('Good morning.')
elif 12 <= currentTime.hour < 18:
    print('Good afternoon.')
else:
   print('Good evening.')

