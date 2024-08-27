'''
def addition(number):
    if number == 1:
        return 0
    return number + addition(number - 1)

function = addition(5)
print(function)
'''

'''
# Examples of valid functions
def subtraction(number):
    return
def subtraction():
    return
def subtraction():
    return "text"
# Examples of invalid function:
def subtraction(number, 5):
    return
'''

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
    return numbers < 50

small_using_filter = list(filter(lesser, numbers))
print(small_using_filter)

small_using_map = list(map(lesser, numbers))
print(small_using_map)

