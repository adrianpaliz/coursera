# Big O Notation
# O(1) Constant time
# Example: Accessing an element ia an array by its index.
courses_provides = ['coursera', 'udemy', 'scrimba']
'''
def access_element(my_list, index):
    return my_list[index]

print(access_element(courses_provides, 1))
'''

# O(n) Liner time
# When you have a runtime that grows linearly with the siza of the input data
# Example: Searching for a specific value in a unsorted list
'''
def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

print(linear_search(courses_provides, 'scrimba'))
'''

# O(n^2) Quadratic time
# Have runtimes that grow with the square of the input size
# Example: A simple sorting algorithm
'''
def bubble_sort(my_list):
    number_items = len(my_list)
    for number in range(number_items):
        for item in range(0, number_items - number - 1):
            if my_list[item] > my_list[item + 1]:
                my_list[item], my_list[item + 1] = my_list[item + 1], my_list[item]

'''

# O(log n) Logarithmic time
# Have runtimes that grow logarithmically with the size of the input data
# Example: Binary search in a sorted list

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(numbers_list, target):
    left = 0 
    right = len(numbers_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers_list[middle] == target:
            return middle
        elif numbers_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return - 1

print(binary_search(numbers_list, 4))

