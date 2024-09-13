def is_present(person):
    names = ['Alfred', 'Bob', 'Carl', 'Martha']
    if person in names:
        return True
    else:
        return False

def no_digit(person):
    if person.isalpha():
        return True
    else:
        return False

