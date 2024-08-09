menu = ['quimbolito', 'bollo', 'cacho', 'empanada', 'bolon', 'corviche']

def find_dish(dish):
    if dish[0] == 'b':
        return dish

# Using map
'''
map_dish = map(find_dish, menu)
print(map_dish)

for dish in map_dish:
    print(dish)
'''
# Using filter

filter_dish = filter(find_dish, menu)
print(filter_dish)

for dish in filter_dish:
    print(dish)

