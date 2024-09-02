# Inheritance and Multiple inheritance
# A simple example of inheritance
class University:
    pass
# Parent class University is passed inside class Students as a parameter
class Students(University):
    pass

# Multiple inheritence
# A simple example
'''
class Buildings:
    # Initialized a variable with a value
    floors = 1

class Houses:
    rooms = 2

class Architecture(Buildings, Houses):
    pass

architecture = Architecture()
print(architecture.floors, architecture.rooms)
'''

# Multi-level inheritance
'''
class Frame():
    size = 10

class Tires(Frame):
    size = 20

class Bike(Tires):
    pass

bike = Bike()
print(bike.size)
'''

# Built-in functions
# We use two built-in functions to trying to find the relationship between different classes and objects
# issubclass()
'''
print(issubclass(Frame, Tires))
print(issubclass(Tires, Frame))
'''
# isinstance()
'''
class Furniture():
    pass
class House():
    pass

house = House()
print(isinstance(house, House))
print(isinstance(house, Furniture))
'''

# The super() built-in function
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)

class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

