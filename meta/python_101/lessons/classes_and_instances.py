# Class definition
class MyClass:
    a = 5
    print('Hello')
# Creating a method inside this class
    def hello(self):
        print('Hello, world!')

# Creating a new instance
myclass = MyClass()

# Ferering to the class object
print(MyClass.a)

# Refering to the instance object
print(myclass.a)

print(myclass.hello())

