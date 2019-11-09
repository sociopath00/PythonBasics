"""
    @author: Akshay Nevrekar
    @created_on: 6th November,2019
    @last_updated_on: 6th November,2019
"""

# import module
import datetime


# get current datetime
print(datetime.datetime.now())

# get current date
print(datetime.date.today())

# create a date
date_obj = datetime.date(2019, 4, 13)
print("Date is", date_obj)

print("Year is", date_obj.year)
print("Month is", date_obj.month)
print("Day is", date_obj.day)

# convert str into datetime
x = "6-11-2019"
print(type(x))

x_datetime = datetime.datetime.strptime(x, "%d-%m-%Y")
print(x_datetime)
print(type(x_datetime))

print(x_datetime.date())

# convert datetime into str
y = datetime.datetime.strftime(x_datetime, "%Y-%m-%d")
print(y)
print(type(y))

# To explore more, refer:  https://www.programiz.com/python-programming/datetime
