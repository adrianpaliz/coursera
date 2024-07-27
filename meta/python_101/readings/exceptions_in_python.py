# IndexError
'''
items = [1, 2, 3, 4, 5]
try:
    ans = items[6]
except IndexError as error:
    print(error, 'item does not exist in the list')
'''

# ZeroDivisionError

def divide_by(a, b):
    return a / b

try:
    result = divide_by(40, 0)
except ZeroDivisionError as error:
    print('0')
except Exception as error:
    print(error, 'something went wrong')

# FileNotFoundError
'''
try:
    with open('my_file.txt', 'r') as file:
        result = file.read()
except FileNotFoundError as error:
    print(error, 'the file could not be found')
'''

