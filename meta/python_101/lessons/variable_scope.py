'''
Different types of scopes:
Local
Enclosing
Global
Built-in
'''

# Global scope
global_variable = 10

def function_1():
    enclosed_variable = 8
    def function_2():

    # Local scope
        local_variable = 5
        print('Access to global variable', global_variable)
        print('Access to enclosed variable', enclosed_variable)
    function_2()

# We can use the function because we are accessing to a global variable
function_1()

# The next line will produce a error because we can't access  to a local variable
# print('Cant access local', local_variable)


