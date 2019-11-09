"""
	@author: Akshay Nevrekar
	@created_on: 5th November,2019
	@last_updated_on: 5th November,2019
"""

marks = {"sam": 79, "dean": 97, "john":57, "stuart": 63}

# check datatype
print(type(marks))

# create empty dicts
a = {}
print(type(a))

b = dict()
print(type(b))

# access values from dict
print("marks of John: ",marks["john"])

print("marks of Stuart: ",marks["stuart"])

# add new key to dict
marks["paul"] = 80
print(marks)

# update value in dict
marks["sam"] = 55
print(marks)

# remove record from dict
marks.pop("john")
print(marks)

## functions
# find keys in dict
print(marks.keys())

# find values in dict
print(marks.values())

# check for value in dict without raising an exception if key not exists
print("marks of Paul: ",marks.get("paul", "Key not present"))
print("marks of John: ",marks.get("john", "Key not present"))

# merge 2 dicts
marks2 = {"dean": 85, "chris": 60, "lyna": 72}
marks.update(marks2)
print(marks)