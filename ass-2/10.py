'''Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)'''

from datetime import datetime
now_date = datetime.today()
print(now_date)

d1 = now_date.strftime("%d-%m-%Y and %I:%M %p")  #for 12 hr format
print(d1)

d2 = now_date.strftime("%d-%m-%Y and %H:%M:%S ")  #for 24 hr format
print(d2)

d3 = now_date.strftime(("%b %d %Y"))
print(d3)

d4 = now_date.strftime(("%B/%d/%y"))
print(d4)