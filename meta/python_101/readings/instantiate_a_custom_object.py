# Exercise: Instantiate a custom object

# Define a class called MyFirstClass
class MyFirstClass:
    # Add a print statement inside it
    print('Who wrote this?')
    # Create a string variable named index
    index = 'Author book'

    # Define a function called hand_list
    # Pass the parameter self to it. and two parameters
    def hand_list(self, philosopher, book):     
        # Write a print statement 
        # and pass the class variable by accessing it
        print(MyFirstClass.index)
        # Write a print statement using built-in concatenation operator
        print(philosopher + ' wrote the book: ' + book)

# Create and instantiate an object of the class
whodunnit = MyFirstClass()
# Call method hand_list() over this object 'whodunnit' and pass two values to it
whodunnit.hand_list('Sun Tzu', 'The Art of War')

