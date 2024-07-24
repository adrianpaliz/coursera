# Using a dictionary
employee_dictionary = {
    12345: {
        'id' : '12345',
        'name' : 'Pedro',
        'department' : 'Kitchen'
    },
    12458: {
        'id' : '12458',
        'name' : 'Carlos',
        'department' : 'House Floor'
    }
}

def get_employee_from_dictionary(id):
    return employee_dictionary[id]

print(get_employee_from_dictionary(12458))

