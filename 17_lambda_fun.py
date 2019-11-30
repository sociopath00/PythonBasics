"""
    @author: Akshay Nevrekar
    @created_on: 10th November,2019
    @last_updated_on:
"""


a = lambda x: x**4
print(a(2))



z = [1,2,3,4]
y = list(map(lambda x: x**4, z))
print(y)



def sqr(val,y):
    return val(y)

print(sqr(lambda x:x*2, 2))
