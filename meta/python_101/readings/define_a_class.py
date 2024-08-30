# Class definition
class Apartment:
    # Data members or attributes
    number_rooms = 3
    bathrooms = 1
    # Function definition(empty)
    def cost_evaluation(self):
        print(self.number_rooms)
        # The pass keyword
        pass
# Instantiating tha class
my_apartment = Apartment()

# A print statement refering to the instance object
print(my_apartment.number_rooms)
# A print statement refreing to the class object
print(Apartment.number_rooms)

# Update the number_rooms variable
# it updates the value of the instance attribute but not the class attribute 
my_apartment.number_rooms = 7
print(my_apartment.number_rooms)
# The number_rooms attribute of the class remains unchanged as 3
print(Apartment.number_rooms)

# Modifying the class attribute 
Apartment.number_rooms = 7
print(my_apartment.number_rooms)
print(Apartment.number_rooms)

