'''
value = 5
class MyClass:
    value = 5
my_class = MyClass()
my_class.value = 3
print(value)
'''
value = 3
my_class = MyClass()
class MyClass:
    value = 5
    print('Inside class MyClass')
my_second_class = MyClass()
print(my_class.value)


