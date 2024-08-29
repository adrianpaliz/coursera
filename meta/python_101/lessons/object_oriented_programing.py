# Pillars of object oriented programming
# Encapsulation
# Polymorphism
# Inheritance
# Abstraction

# Encapsulation
'''
class Alpha:

def __init__(self):
    self._a = 2.  #Protected member 'a'
    self.__b = 2.  #Private member 'b'
'''

# Polymorphism
'''
string = 'poly'
number = 7
sequence = [1, 2, 3]

new_string = string * 3
new_number = 7 * 3
new_sequence = sequence * 3
print(new_string, new_number, new_sequence)
'''

# Inheritance
# A basic template as example
'''
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class
'''

# Abstraction
# A simple implementation as example
from abc import ABC,
class ClassName(ABC):
    pass



