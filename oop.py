
# ===================================
# Object Oriented Programming (OOP)
# ===================================

# ===================================
# Introduction to Classes
# ===================================

# There are several programming paradigms.
# (1) Imperative:
# - involves providing a series of instructions for the computer to follow in a defined order.
# - We have been using this

# (2) Object oriented programming
# - Aims to combine data processes that act on that data into objects
# - This is called encapsulation
#

# These two programming paradigms are not mutually exclusive. Imperative uses OOR and OOR uses imperative style

# NOTE that everything in python is an object.
# In the program below, even though a and b are integer variables, the do have method __add__ to them (and others)
# If you CTRL + and CTRL __add__, you find they go to the same built in function "def __add__(self, *args, **kwargs):"
# This is the built in definition of the add method.

# a = 12
# b = 10
# print(a + b)
# print(a.__add__(b))



# OOP uses classes and methods to provide objects that encapsulate both data and the function that operate on that data.
# "Method" is just another word for "Function".

# When a function is part of a class, we call it a "Method"
# In python, there is a slight difference between a "function" and a "Method"
# But writing a method is te same as writing a function


# =================================
# Classes in python
# =================================

# We will use a simple example about implementation of the electric kettle

# We will start by creating a "KettleClass" class, that will model a kettle

# We can think of a class as a template from which objects can be created.
# All the objects created from the same class will share the same characteristics.

# When we create objects of this "KettleClass" class, they will have a name (make) and price.

# An instance is just another name for an object created from a class definition.
# Each instance of the class will have its own values for name and price.

# So if we create a kettle called Kenwood, then Kenwood will be an instance of the "KettleClass" class
# We can also say "kenwood" is an object of type "KettleClass"

# Define class called KettleClass which is passed an object
# Once a class has been defined, you can create as many instances of the class as you want.
# NOTE that you can only use the class defined to create instances of the class
# Once the instances have been created, you can then call their method and access their variables.

# =====================
# Summary definitions
# =====================

"""
Class:  Template for creating objects. All objects created using the same class will have the same characteristics
Object:  An instance of a class
Instantiate:  Create an instance of a class
Method:    A function defined in a class
Attribute: A variable bound to an instance of a class
"""
#
#
# class KettleClass(object):
#
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False  # initially self.on was set to False
#
#
#     # As we add this switch_on "method", we see it automatically adds (self)
#     # Functions that are bound to a class are called "Methods" and the main difference between a "Method" and
#     # a "function" is the presence of this (self) parameter that is added automatically in "Method"
#
#     # NOTE: "self" is just a name of a parameter. you can name it whatever but it is sdvisable to leave it as "self"
#     # "self" is a reference to the instance of the class.
#     # We will call this "switch_on" Method down below.
#
#     def switch_on(self):
#         self.on = True  # Set self.on to True
#
#
#
# # Now we will create a Kettle Object called kenwood.
# # We will pass them two parameters, (make and price)
#
# kenwood = KettleClass("kenwood", 8.99)  # Creates an instance of KettleClass class and we name it kenwood
# print("Make  = {}".format(kenwood.make))   # Call method kenwood and access variable make
# print("Price = ${}".format(kenwood.price))   # Call method kenwood and access variable price
#
# # We can even adjust the price
# kenwood.price = 12.50
# print("New Price = ${}".format(kenwood.price))  # Call method kenwood and access variable price
#
#
# # We will create another kettle instance called hamilton
#
# hamilton = KettleClass("hamilton", 20.55)  # Creates an instance of KettleClass class and we name it hamilton
# print("="*20)
# print("Hamilton price = {}".format(hamilton.price))
#
# # We can print all of them in one line
# # We will get the "make" and "price" attributes of the "kenwood" and "hamilton" objects.
#
# print("="*20)
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
#
#
# # There is another way to use string replacement fields when dealing with classes
# # Because kenwood and hamilton are objects, we can specify their attributes in the replacement fields {}
#
# print("="*20)
# print("Specifying attributes in replacement fields")
# print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))
#
# # Here we will print the "self.on" instance for both kenwood and hamilton
# # then change it with the switch_on function/method
#
# # Initial hamilton.on is False because that is what it was initialized in the "Constructor".
# # NOTE: "Constructor" refers to a special method that is executed when an instance of a class is created of constructed.
# # In python, the "Constructor" is the __init__ method
#
#
# print("="*20)
# print("Initial hamilton.on = {}".format(hamilton.on))  # This should show False because that is what it was initialized in the "Constructor"
#
# # Now we call on switch_on Method for hamilton instance that changes its "self.on" parameter to True
# # MOTE when we call hamilton.switch_on(), we don't provide a value for the "self" parameter under ()
# # this is because when you call a method on an instance, python automatically provides a reference to the
# # instance as the first parameter to the method
#
# hamilton.switch_on()
#
# # print the new hamilton.on
# print("New hamilton.on = {}".format(hamilton.on))  # This will show True
#
#
# # We can also call method hamilton from the class
#
# print("="*20)
# print("Initial kenwood.on = {}".format(kenwood.on))  # Result will be False
#
# # Now we call method switch_on from KettleClass and we need to give it a parameter (kenwood)
# # so it knows what instance to change self.on switch for
#
# KettleClass.switch_on(kenwood)
#
# print("New kenwood.on = {}".format(kenwood.on))  # Result will be True
#
#
# # ==============================
# # Adding new instance variables
# # ==============================
#
# # NOTE that variables in python come into existence the first time they are assigned a value.
# # Instance variables also come into existence the first time they are assigned a value.
#
# # We will create a new "instance variable" for "kenwood" called "power"
# # so instance variable "power" is bound to instance "kenwood" of the "KettleClass"
#
# kenwood.power = 1.5  # We assign power to kenwood to be 1.5 watts
# print("="*20)
# print("kenwood.power = {}".format(kenwood.power))  # This Will print 1.5
#
# # if you try to print hamilton.power, it will give error because hamilton.power variable was not created and does not exist
# # We did not create that variable by assigning a value to it.
# # This is the dynamic nature of python that allows this kind of behavior where you can end up with instances created
# # from the same class template but have different attributes e.g. we now have kenwood.power but don't have hamilton.power
# # and they were both created from KettleClass class template
# # However "subClassing" - where a new class is created from an existing one may be preferable to adding attributes to instances
# # We will look at subclassing a little later.
#
#
# # print("hamilton.power = {}".format(hamilton.power))


# ================================================================
# preventing additional attributes from being added to instances
# ================================================================

# There are ways to prevent above behavior where attributes are added to class instances
# You can create classes in such a way that additional attributes cannot be added to instances
# This will force classes to be subclassed when extra functionality is required


# =======================
# other aspects of class
# =======================

# We referred to "instance variable" previously because it includes the word "variable"
# whearas "data attribute" does not.
# this is important because "methods" are "attributes" of classes
# The term "attribute" is used to refer to both in the documentation
# The term "data attribute" and "method" are used to distinguish between the two types of attributes.

# =======================
# other aspects of class
# =======================

# Classes also have attributes.
# Hence term "instance variable" is also useful here because it contains the words "instance"

# The data attribute in the "KettleClass" e.g. make and price, have both been attributes of the instances
# and each instance has its own values for them.

# ==========================
# Class attributes
# ==========================

# It is also possible for a class to have "attributes" that are shared by all the instances.
# Here we will introduce a class attribute called "power_source" to show the power source of the kettles


class KettleClass(object):

    # Class attribute power_source will be shared by all class instances from class KettleClass
    # We can go at the bottom to show that all instances now have power_source
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False  # initially self.on was set to False

    def switch_on(self):
        self.on = True  # Set self.on to True

# Now we will create a Kettle Object called kenwood.
# We will pass them two parameters, (make and price)

kenwood = KettleClass("kenwood", 8.99)  # Creates an instance of KettleClass class and we name it kenwood
print("Make  = {}".format(kenwood.make))   # Call method kenwood and access variable make
print("Price = ${}".format(kenwood.price))   # Call method kenwood and access variable price

# We can even adjust the price
kenwood.price = 12.50
print("New Price = ${}".format(kenwood.price))  # Call method kenwood and access variable price


# We will create another kettle instance called hamilton

hamilton = KettleClass("hamilton", 20.55)  # Creates an instance of KettleClass class and we name it hamilton
print("="*20)
print("Hamilton price = {}".format(hamilton.price))

# We can print all of them in one line
# We will get the "make" and "price" attributes of the "kenwood" and "hamilton" objects.

print("="*20)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("="*20)
print("Specifying attributes in replacement fields")
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print("="*20)
print("Initial hamilton.on = {}".format(hamilton.on))  # This should show False because that is what it was initialized in the "Constructor"

# Now we call on switch_on Method for hamilton instance that changes its "self.on" parameter to True
hamilton.switch_on()

# print the new hamilton.on
print("New hamilton.on = {}".format(hamilton.on))  # This will show True


# We can also call method hamilton from the class

print("="*20)
print("Initial kenwood.on = {}".format(kenwood.on))  # Result will be False

# Now we call method switch_on from KettleClass and we need to give it a parameter (kenwood)

KettleClass.switch_on(kenwood)

print("New kenwood.on = {}".format(kenwood.on))  # Result will be True


# ==============================
# Adding new instance variables
# ==============================

# NOTE that variables in python come into existence the first time they are assigned a value.
# Instance variables also come into existence the first time they are assigned a value.

# We will create a new "instance variable" for "kenwood" called "power"
# so instance variable "power" is bound to instance "kenwood" of the "KettleClass"

kenwood.power = 1.5  # We assign power to kenwood to be 1.5 watts
print("="*20)
print("kenwood.power = {}".format(kenwood.power))  # This Will print 1.5

# if you try to print hamilton.power, it will give error because hamilton.power variable was not created and does not exist
# print("hamilton.power = {}".format(hamilton.power))

# We check here to see if all KettleClass instances (kenwood & hamilton) have power_source
# Results show Class and instances of class all have shows power_source of electricity, that was defined in KettleClass

print("="*20)
print("power sources:")
print("="*14)
print("KettleClass.power_source = {}".format(KettleClass.power_source))
print("kenwood.power_source     = {}".format(kenwood.power_source))
print("hamilton.power_source    = {}".format(hamilton.power_source))

# We can also check the namespaces of the three objects above to verify
# that the two instances are sharing the same attributes which only exist in the class
# We can access the "namespace" using the __dict__ attribute

print("="*45)
print("Checking namespaces using __dict__ attribute:")
print("="*45)
print(KettleClass.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

# results are as follows
# for kenwood ==> {'make': 'kenwood', 'price': 12.5, 'on': True, 'power': 1.5}
# for hamilton ==> {'make': 'hamilton', 'price': 20.55, 'on': True}

# NOTE that only KettleClass has attribute power_source
# Kenwood has extra power because we added attribute power.

# When we try to access the power_source for the instances e.g. hamilton.power_source and kenwood.power_source,
# Python checks to see if the attribute exist in the instance namespace (in this case, it does not)
# If it does not, python then checks the class for power_source in the KettleClass class
# This is why it is able to print it out as "electricity" because it got it from the class

# =============================
# Modifying attribute in Class
# =============================

# We can modify the "power_source" attribute in the class KettleClass
# We see that power for all instances change to Atomic power.
# Proof that the instances are deriving power attribute from the class


print("="*45)
print("Switch power source to atomic in KettleClass:")
print("="*45)
KettleClass.power_source = "Atomic Power"
print("KettleClass.power_source = {}".format(KettleClass.power_source))
print("kenwood.power_source     = {}".format(kenwood.power_source))
print("hamilton.power_source    = {}".format(hamilton.power_source))



# =============================
# Modifying attribute in Instance
# =============================

# We will modify power source for instance hamilton to Gas power
# The results show that only hamilton.power_source is modified to Gas Power
# Also note that hamilton now has attribute power_source, because when we modified attribute power_source,
# python created a local variable named power_source and added it to instance hamilton


print("="*45)
print("Switch power source to Gas in hamilton:")
print("="*45)
hamilton.power_source = "Gas Power"
print("KettleClass.power_source = {}".format(KettleClass.power_source))
print("kenwood.power_source     = {}".format(kenwood.power_source))
print("hamilton.power_source    = {}".format(hamilton.power_source))  # Result is gas power
print(KettleClass.__dict__)
print(kenwood.__dict__)  # No attribute power_source since its deriving attribute from KettleClass.
print(hamilton.__dict__)  # We can also see there is attribute power_source here, since we modified/created it.












