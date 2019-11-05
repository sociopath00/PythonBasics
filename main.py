"""
	@author: Akshay Nevrekar
	@created_on: 5th November,2019
	@last_updated_on: 5th November,2019
"""

a = ("a",15,33, True,"hello",17.9998)
b = (False,"train",90.01,33)

# check datatype
print(type(a))

# create an empty tuple
# In practice, this is not useful as tuples are immutable
c = tuple()
print(type(c))

d = ()
print(type(d))


## indexing
print(a[0])

print(a[2])

print(a[-1])


## slicing
print(a[1:4])

print(a[:3])

print(a[2:])


# concatenate 2 tuples
print(a+b)

# repeat elements
print(a*2)


## Functions
x = a.index(True)
print(x)

y = a.count("hello")
print(y)