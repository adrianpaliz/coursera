# Reversing a string
# There are two ways to reverse a string in Python

# Using the Slice function
# The extended slice syntax 
    #str[start : stop : step]
'''
my_string = "reversal"
my_string_copy = my_string[::-1]
print(my_string_copy)
'''

# Using Recursion

def string_reverse(string):
    if len(string) == 0:
        return string
    else:
        return string_reverse(string[1:]) + string[0]

string = "reversal"
reverse = string_reverse(string)
print(reverse)

