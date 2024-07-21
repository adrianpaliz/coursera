list_1 = [1, 2, 3, 4, 5]
# Printing a list item (gets the third item ased on his index)
#print(list_1[2])

list_2 = ['A', 'B', 'C']

# List of diferent data types
list_3 = ['Hello', 1, True, 40.22]

# Nested lists
list_4 = [1, [2, 3, 4], 5, 6]

# Printing lists
print(*list_1) # The entire list is printed out
print(*list_1, sep = '^')

# Adding items to a list
# Using insert method
list_1.insert(len(list_1), 6)
print(list_1)
# Using append method
list_1.append(7)
print(list_1)
# Using extend method
list_1.extend([8, 9, 10, 11])
print(list_1)

# Removing items
# Using pop method
list_1.pop() # If the index is not specified the last item is removed
print(list_1)
list_1.pop(8) # The index is specified
print(list_1) 
# Using del statement 
del list_1[5] 
print(list_1)

# Iterating through the list
for item in list_1:
    print('Value: ', item)

