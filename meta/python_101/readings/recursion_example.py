# Recursive function for Tower of Hanoi

# Function definition
def tower_of_hanoi(disks, source, helper, destination):
    
    # Base condition
    if disks == 1:
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    tower_of_hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    tower_of_hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))

# Actual function call
tower_of_hanoi(disks, 'source', 'helper', 'destination')
