a = {1,2,3,4,5}
b = {8,6,12,4,5}
c = {1,3,5}
d = {9,12,11}

# check datatype
print(type(a))

# empty set
e = set()
print(type(e))

## set properties
# union
print("A union B: ",a.union(b))
print("C union B: ", c | b)

# intersection
print("A intersection B: ",a.intersection(b))
print("C intersection B: ",c & b)

# difference
print(a.difference(b))
print(a - b)
print(b - a)

# disjoint
print(a.isdisjoint(d))
print(a.isdisjoint(c))

# subset
print(c.issubset(a))
print(b.issubset(a))
"""
	@author: Akshay Nevrekar
	@created_on: 5th November,2019
	@last_updated_on: 5th November,2019
"""

a = {1,2,3,4,5}
b = {8,6,12,4,5}
c = {1,3,5}
d = {9,12,11}

# check datatype
print(type(a))

# empty set
e = set()
print(type(e))

## set properties
# union
print("A union B: ",a.union(b))
print("C union B: ", c | b)

# intersection
print("A intersection B: ",a.intersection(b))
print("C intersection B: ",c & b)

# difference
print(a.difference(b))
print(a - b)
print(b - a)

# disjoint
print(a.isdisjoint(d))
print(a.isdisjoint(c))

# subset
print(c.issubset(a))
print(b.issubset(a))
