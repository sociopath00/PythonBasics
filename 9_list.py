"""
    @author: Akshay Nevrekar
    @created_on: 5th November,2019
    @last_updated_on: 5th November,2019
"""

l1 = [100, 34.5, "python", True]
l2 = [-12, 0.0, False, "java"]
# check datatype
print(type(l1))

# create an empty list
l3 = []
print(type(l2))

l4 = list()
print(type(l3))

# concatenate two list
print("concatenate l1 and l2: ",l1 + l2)

# repeat the elements in l1 3 times
print("Repeat l1 elements: ",l1 * 3)

## Note: above operations do not affect on original lists


## indexing  (indexing starts from 0)
# access 1st element in the list
print(l1[0])

# access 3rd element in the list
print(l1[2])

# access last element in the list
print(l1[-1])


## Slicing
# access 2nd to 4th elements from the list
print(l1[1:4])

# access 1st 3 elements in the list
print(l1[:3])

# access 2nd element onwards
print(l1[1:])

# reverse the list
print(l1[::-1])


## List Functions
# add element in the list
l1.append(23)
print(l1)

l1.append(l2)
print(l1)

l1.extend(l2)
print(l1)

# remove elements from the list
l1.remove(-12)
print(l1)

l1.remove(l2)
print(l1)

# pop removes the element at specified index from the list
# and returns the value which has been removed
x = l1.pop(2)
print("Removed element: ",x)
print(l1)

# removes last element in the list
l1.pop()
print(l1)

# find the index of specific element
idx = l1.index(23)
print(idx)

# insert element at given index
l1.insert(2, 100)
print(l1)

# count the occurance of element
count = l1.count(100)
print(count)

# copy the list element
l1_copy = l1.copy()
print(l1_copy)

# clear the elements of list
l1.clear()
print(l1)
