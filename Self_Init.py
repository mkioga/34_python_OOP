
# ========================================================
# Understanding Self and __init__ Methods in python class
# ========================================================

# https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

# =======
# Class:
# =======
#
# Class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.
# In technical terms we can say that class is a blue print for individual objects with exact behaviour.
#
# =========
# Object:
# =========
#
# object is one of instances of the class. which can perform the functionalities which are defined in the class.
#
# =======
# self:
# =======
#
# self represents the instance of the class.
# By using the "self" keyword we can access the attributes and methods of the class in python.
#
# ===========
# __init__ :
# ===========
#
# "__init__" is a reseved method in python classes.
# It is known as a constructor in object oriented concepts.
# This method is called when an object is created from the class and it allow the class to initialize the attributes of a class.


# ==============================
# How can we use  "__init__ " ?
# ==============================

# Let's consider that you are creating a NFS game. for that we should have a car. ' \
# 'Car can have attributes like "color", "company", "speed_limit" etc. and methods like "change_gear", "start", "accelarate", "move" etc.

# This is the Car class

class Car(object):
    """ Blueprint for a Car """

    def __init__(self, model, color, company, speed_limit):  # initialize attributes of class to object
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("Accelerating ... ")
        " accelerator functionality here"

    def change_gear(self):
        print("gear changed")
        "gear related functionality here"


# Now we create different models of cars using the Car Class as template
# We have created two different types of car objects with the same class.
# While creating the car object (toyota) we passed arguments  "Camry", "red", "Toyota Motors", 70
# These arguments will pass to "__init__" method  to initialize the object "toyota".
# Here, the magic keyword "self"  represents the instance of the class i.e. toyota.
# It binds the attributes with the given arguments.

toyota = Car("Camry", "red", "Toyota Motors", 70)
suzuki = Car("Maruti", "White", "Suzuki Motors", 60)

# We can print to see how the self initialized the object "toyota"
print(toyota)
print(toyota.model)
print(toyota.color)
print(toyota.company)
print(toyota.speed_limit)
print(toyota.accelerate())
print(toyota.change_gear())

print()
print("="*30)
print()

# ===========================================================
# Using "self" in class to access the methods and attributes
# ===========================================================

# Find out the cost of a rectangle

# We create Class named Rectangle

class Rectangle:

    # ___init__ method to assign parameters length, width, unit_cost to an instance of class that is created later

    def __init__(self, length, width, unit_cost=0):  # we initialize unit cost to 0
        self.length = length  # Self is used to bind the passed parameters to the object
        self.breadth = width
        self.unit_cost = unit_cost

    # Function to get perimeter of rectangle

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    # Function to get area of rectangle

    def get_area(self):
        return self.length * self.breadth

    # Function to calculate area = area x unit cost

    def calculate_cost(self):
        area = self.get_area()  # Gets the area of Rectangle
        return area * self.unit_cost  # Calculates cost and returns it

# Now we make object called "Rectangle_1" and give it the following arguments
# length = 20, width = 10, unit_cost = 2

Rectangle_1 = Rectangle(20, 10, 2)

print("Area of Rectangle_1 = {}".format(Rectangle_1.get_area()))
print("Cost of Rectangle_1 = {}".format(Rectangle_1.calculate_cost()))


