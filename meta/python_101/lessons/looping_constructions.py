#for index in range(5):
#    print('Looping...', index)

favorites = ['Cuy', 'Tigrillo', 'Bandera', 'Bolón', 'Chicha']

#for item in favorites:
#    print('I like this meal', item)
#for index, item in enumerate(favorites):
#    print(index, item)

'''
count = 0
while count < len(favorites):
    print('I like this meal', favorites[count])
    count += 1
'''
'''
for item in favorites:
    if item == 'Bandera':
        print('Yes! one of my favorite meals is', item)
        continue
    else:
        print('No sorry, that meal is not on my list')
'''

for item in favorites:
    if item == 'Bandera':
        pass
    print('Other meal I like is', item)


