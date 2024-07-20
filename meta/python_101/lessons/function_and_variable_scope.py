'''
Local scope:
Refers to a variable declared inside a function.
In the code below "total" is only available to the code within the "get_total" function
'''
def get_total(a, b):
    # Local variable declared inside a function
    total = a + b
    return total
print(get_total(5, 2))

# Accessing variable outside of the function: (The next line will generate a NameError)
#print(total)

'''
Enclosing scope:
Refers to a function inside another function or nested function
In the code below "double" varaible cannot be accessed from inside the get_total function
'''
def get_total(a, b):
    # Enclosed variable declared inside a function
    total = a + b
   
    def double_it():
        # Local variable
        double = total * 2
        print(double)
    
    double_it()
    # double variable will not be accessible    
    #print(double)
    return total # Always a function has to return something
print(get_total(4, 2))

'''
Global scope
Is when a variable is declared aoutside of a function, can be accessed from anywhere.
In the code below the variale "special" can be accesses from both functions.
'''
global_variable = 5

def get_total(a, b):
    # Enclosed scope variable declared inside a function
    total = a + b
    print(global_variable)

    def double_it():
        # Local varaible
        double = total * 2
        print(global_variable)
    double_it()

    return total
print(get_total(1, 5))

