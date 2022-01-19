# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)
from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(14122021)
print("Datetime from timestamp:", date_time)
from datetime import date

# calling the today
# function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
# Python program to
# demonstrate time class

from datetime import time

# calling the constructor
my_time = time(13, 24, 56)

print("Entered time", my_time)

# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)

# Uncommenting time(hour = 26)
# will rase an ValueError as
# it is out of range

# uncommenting time(hour ='23')
# will raise TypeError as
# string is passed instead of int
from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

