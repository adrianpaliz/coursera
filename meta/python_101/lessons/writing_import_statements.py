# Importing a built-in method
import sys

# Using a function that is inside of a method
import random

random_integer = random.randint(3, 9)
print(random_integer)

# Directly importing a function of a method
from math import sqrt

root = sqrt(9)
print(root)

# Importing using an alias for the module
from datetime import datetime as dates

current_time = dates.now()
print(current_time)

# Importing many functions
from string import ascii_letters, digits

letters = (ascii_letters)
print(letters)
digits = (digits)
print(digits)

# Importing all the function inside a given module
from os import *

directory = getcwd()
print(directory)


