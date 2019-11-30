"""
    @author: Akshay Nevrekar
    @created_on: 30th Nov, 2019
    @last_update_on:
"""

# generator functions
# return a square of each element of list

def list_square(ls):
    for l in ls:
        yield l*l


a = [1,2,3,5]
print(list_square(a))

# fetching a value one by one
sq = list_square(a)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))


# get all the values once
sq2 = list(list_square(a))
print(sq2)


# list comprehension as generator
sq3 = (i*i for i in a)
print(sq3)

