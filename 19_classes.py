"""
    @author: Akshay Nevrekar
    @created_on: 2nd December,2019
    @last_updated_on:
"""


# simple class
class ClassOne:
    var1 = 12
    var2 = 24

# create object
c1 = ClassOne()
print("Value of variable 1:",c1.var1)

# create 2nd object
c2 = ClassOne()
print("Value of variable 2:",c2.var2)


###########################################

# class with constructor (and instance variable)
class ClassSquare:
    def __init__(self, side):
        self.side = side

# creating a object with side=5
s1 = ClassSquare(5)
print("Side of square:",s1.side)


##########################################

# class with instance methods
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    # instance method
    def area(self):
        return self.l*self.b

r1 = Rectangle(12, 4)
print("Area of Rectangle: ", r1.area())

###########################################

# class with class variable
class Circle:
    pi = 3.14  # class variable

    # constructor
    def __init__(self, radius):
        self.radius = radius

    # instance method
    def area(self):
        return Circle.pi * self.radius**2

c1 = Circle(12)
print("Area of circle:", c1.area())
Circle.pi = 34

c2 = Circle(5)
print(c2.pi)


#########################################

# class with static method
class HelloWorld:
    @staticmethod
    def printstr():
        print("Hello World!!!")

hw = HelloWorld()
hw.printstr()
