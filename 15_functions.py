"""
    @author: Akshay Nevrekar
    @created_on: 24th November,2019
    @last_updated_on:
"""

# defining function with single parameter
def circle_area(radius):
    area = 3.14*radius*radius
    return area

# calling a function
c_area = circle_area(radius=5)
print(c_area)


# defining function with 2 parameters
def rect_area(l,b):
    area = l*b
    return area

# calling a function
ra = rect_area(8, 2)
# print(ra)


# function to find average of a list
a = [1,2,3,4,5]

def avg(inp):
    ag = sum(a)/len(a)
    return ag

print(avg(a))



# def is_even(no):
#     if no%2==0:
#         return True
#     else:
#         return False

# print(is_even(15))

# def percentage(no1, no2):
#     return no1/no2*100

# def grades(marks, total):
#     marks =  percentage(marks, total)
#     if marks > 100:
#         return "Enter correct marks"
#     elif marks >= 60:
#         return "1st class"
#     elif 40 <= marks < 60:
#         return "2nd class"
#     else:
#         return "Fail"

# print(grades(80,150))

# print(percentage(20,50))



