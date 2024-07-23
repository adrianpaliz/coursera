# We declare a set 
set_1 = {1, 2, 3, 4, 5}
# Printing a set
#print(set_1)

# Sets don't allow duplicate values
set_2 = {4, 5, 5, 6, 7, 8}
# The next line will print only one 5
#print(set_2)

# Set also have methods
# For add new content
set_1.add(6)
#print(set_1)
# For remove items
set_1.remove(2)
print(set_1)
# discard method do the same as remove
set_2.discard(6)
print(set_2)
# For join the two sets without duplicates
#print(set_1.union(set_2))
# Also for join we can use the OR simbol
print(set_1 | set_2)
# Another operation is the intersection: We get back all the items that match in both sets
#print(set_1.intersection(set_2))
# intersection can also be represented by the ampersand
print(set_1 & set_2)
# Another methos is difference: We get back only items that are in set 1 and not in set 2
#print(set_1.difference(set_2))
# We also can represent difference with symbol minus
print(set_1 - set_2)
# Another method is symmetric difference: we get back all of the elements that are presented in set 1 or set b but not in both sets
#print(set_1.symmetric_difference(set_2))
# We can also represent symmetric difference with the carrot operator
print(set_1 ^ set_2)

# We can not print out content based on index
# The next line will generate a TypeError
#print(set_2[0])

