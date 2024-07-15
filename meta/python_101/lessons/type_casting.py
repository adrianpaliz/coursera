# Converting the specified value into a string
'''
integer = 11
print(str(integer))
'''
# Converting into a integer
'''
float_value = 20.5
print(int(float_value))
'''
# Converting into a float
'''
integer = 5
print(float(integer))
'''
# Simple example of converting data, will print the boolean value True
#print(10 == 10)

# Implicit type conversion
# In the next line these are the same numbers but they are not the same data types
#print(10 == 10.00)
# Python implicitly converts integers to float, and then completes the operation
'''
print(10 + 10.00)
print(type(10+10.00)) # It's a float
'''
'''
number_1 = input('First number is: ')
number_2 = input('Second number is: ')
user_sum = number_1 + number_2 # We are adding strings
print(user_sum)
# It's the same as if we just did this:
hard_code_n_1 = '5'
hard_code_n_2 = '3'
numbers_sum = hard_code_n_1 + hard_code_n_2
print(numbers_sum)
'''
# Converting the value of '5' to the value of 5
number_1 = input('First number is: ')
number_2 = input('Second number is: ')
user_sum = float(number_1) + float(number_2)
#print(user_sum)
# Output some words to the user
#print('The sum of: ' + number_1 + ' and ' + number_2 + ' is ' + user_sum) #This will throw a TypeError, We cannot concatenate a string and a float, works when we use strings and integers.
# Solution
print('The sum of ' + str(number_1) + ' and ' + str(number_2) + ' is ' + str(user_sum))

