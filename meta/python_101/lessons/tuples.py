# Tuples
# To declare a tuple we use parentheses
# Tuples can collec any kind of data
tuple_1 = (1, 'string', 4.5, True)
# We can declare a tuple without parentheses, however it's best practice to use parentheses
tuple_2 = 3.2, False, 'string_2', 2
# We can access to a item using index
print(tuple_1[1])

# To determinate the type of the tuple
print(type(tuple_1))

# Counting the number of occurrences of a value
print(tuple_2.count('string_2'))

# Getting the index of a value
print(tuple_2.index(2))

# Iterating through a tuple
for value in tuple_2:
    print(value)

# One of the key difference of a tuple over a list is that tuples values are immutable, they cannot be changed
# We can try to re asign a item, the next line will produce an TypeError
#tuple_1[0] = 5

