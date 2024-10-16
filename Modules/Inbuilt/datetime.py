#Datetime module

import datetime
from datetime import date

# get the current date and time
now = datetime.datetime.now()

print(now)

# get current date
current_date = datetime.date.today()

print(current_date)

# today() to get current date
todays_date = date.today()

print("Today's date =", todays_date)

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))