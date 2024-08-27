# Comprehensions

# List comprehension
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# Example 1: Updating the same list
'''
numbers = [number + 2 for number in numbers]
print('Updating the list: ', numbers)
'''
# Creating a different list with updated values
'''
numbers_new = [number * 3 for number in numbers]
print('Creating new list: ', numbers_new)
'''
# With an if-condition: multiples of four:
'''
multiples_of_two = [number for number in numbers if number % 2 == 0]
print('Divisible by two', multiples_of_two)
'''
# Updating the list with the if condition 
'''
multiples_of_two_minus_one = [number - 1 for number in numbers if number % 2 == 0]
print('Divisible by two minus one: ', multiples_of_two_minus_one)
'''
# Using range function:
'''
sevens = [number for number in range(50) if number % 7 == 0]
print('Sevens: ', sevens)
'''
# Writting the same code using the conventional for loop and if else conditions
# For instance, in the case of example 1:
# Using list comprehension
'''
numbers = [number + 2 for number in numbers]
print(numbers)
'''
# Regular for loop
'''
for number in range(len(numbers)):
    numbers[number] = numbers[number] + 2
print(numbers)
'''

# Dictionary comprehension
# Using range() function and no input list
'''
using_range = {number : number * 3 for number in range(5)}
print('Using range() function: ', using_range)
'''
# Lists
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
numbers = [1, 2, 3, 4, 5, 6, 7]
# Using one input list
'''
num_dict = {number : number ** 2 for number in numbers}
print('Using one input list to create a dict: ', num_dict)
'''
# Using two input lists
'''
days_dict = {key : value for (key, value) in zip(numbers, days)}
print('Using two lists: ', days_dict)
'''

# Set comprehension
# Very similar to list comprehension, the difference is the use of curly brackets for sets instead of square brackets
'''
set_a = {number for number in range(10, 20) if number not in [11, 15, 19]}
print('Numbers in range 10 to 20, without 11, 15, 19: ', set_a)
'''

# Generator comprehension
# Very similar to list
# With the variation of using curved brackets instead of square brackets
# More memory efficent as compared to list comprehension
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
gen_obj = (number for number in numbers)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = ' ')

