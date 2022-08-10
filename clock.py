# - * - coding:utf-8

import datetime
from playsound import playsound

time_now = datetime.datetime.now()

print(time_now)

print('Day')
day = str(input())
print('Hour')
hour = str(input())
print('Min')
minutes = str(input())

while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour) == hour and str(time_now.minute) == minutes and str(time_now.day) == day:
        playsound("C:/dababy.mp3")
        break