milk = input('Do you like to add milk? (y/n): ')
sugar = input('Do you like sugar? (y/n): ')

cup = []
hot_water = True

def make_instant_coffee():
    if hot_water:
        cup.append('hot water')
        cup.append('coffee')
        if milk == 'y':
            cup.append('milk')
        if sugar == 'y':
            cup.append('sugar')
        return print(cup)
    else:
        return print('Wait until water is boiling')

make_instant_coffee()

