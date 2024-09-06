def mammal():
    animal = 'bat'
    
    def quadrupeds():
        nonlocal animal
        animal = 'girafe'
        print('Inside nested function quadrupeds: ' + animal)

    print('Before calling function quadrupeds: ' + animal)
    quadrupeds()
    print('Afther nested function: ' + animal)

animal = 'whales'

mammal()
print('Global animal: ' + animal)

