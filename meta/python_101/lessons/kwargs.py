# args
# With args you could pass in any amount of non-keyword variables
# Example function
def sum_two_values(a, b):
    return a + b
print(sum_two_values(3, 5))
# If we want to add another value, we will have a TypeError
#print(sum_two_values(3, 5, 4))
# Here is were args are useful
def sum_values(*args):
    total = 0
# We have to create a simple for loop
    for value in args:
        total += value
    return total
# Now we can pas any number of arguments to the function
print(sum_values(3, 5, 4, 1, 7))

# kwargs
# With kwargs you can pass in any amount of keyword arguments
# Let's say you wanted to calculate a total bill for a restaurant
def sum_bill(**kwargs):
    total = 0
# We have to change our for loop
    for key, value in kwargs.items():
        total += value
    return round(total, 2)
print(sum_bill(tigrillo = 3.99, jugo = 1.35, salprieta = 0.99))

