# Class definition
class MyClass:
    a = 5
    print('Hello')
# Creating a method inside this class
    def hello(self):
        print('Hello, world!')

# Creating a new instance
my_class = MyClass()

# Ferering to the class object
print(MyClass.a)

# Refering to the instance object
print(my_class.a)

print(my_class.hello())

