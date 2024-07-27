# Explore two types of error
# Syntax error: which are caused by human errors (misspelling or typo)
# A commom error for new developers learning in Python is not adding the colon at the end of conditions or statements
# Other commom mistake is indentation problems

# Exceptions: which are known errors that need to be handled

# Example
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except Exception as error:
    print("Something went wrong!", error)
    print(error.__class__)

