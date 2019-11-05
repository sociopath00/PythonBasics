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
print("A difference B: ",a.difference(b))
print("B difference A: ",b - a)

# disjoint
print("A and D are disjoint sets: ",a.isdisjoint(d))
print("A and C are disjoint sets: ",a.isdisjoint(c))

# subset
print("C is subset of A: ",c.issubset(a))
print("B is subset of A: ",b.issubset(a))

# superset
print("A is superset of C: ",a.issuperset(c))
print("C is superset of A: ",c.issuperset(a))

# add element
a.add(99)
print(a)

# remove element
a.remove(5)
print(a)

a.pop()
print(a)

# clear elements
a.clear()
print(a)