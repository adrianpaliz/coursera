# Pure functions:
# Is a function that does not change or have any effect on a variable, data, list, or sets beyond its own scope.
# Example

my_random_list = [1, 'apple', "3", 'h']

def add_to_list(my_list, item):
    # Don't change the global list, we create a new list
    new_list = my_random_list.copy()
    new_list.append(item)
    return new_list

print(add_to_list(my_random_list, 'sugar'))

