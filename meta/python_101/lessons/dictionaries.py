# Dictionaries
dictionary_1 = {
    1 : 'Chinivi',
    2 : 'Echeandía',
    3 : 'Bolívar',
    4 : 'Ecuador',
    2 : 'Balsapamba'
}
print(type(dictionary_1))
# Duplicated keys are not allowed, the key will be averwritten with the latest one.
print(dictionary_1)
# We can have string key values
dictionary_1['sample_key'] = 'South america'
# We access values based on keys, using the key value path
print(dictionary_1[1])
# Values can be update
dictionary_1[2] = 'Caluma'
print(dictionary_1)
# We also can delete an item using delete function
del dictionary_1[3]
print(dictionary_1)

# Iterating over a dictionary:
# Standard iteration method, only prints the keys
for key in dictionary_1:
    print(key)
# items function
for key, value in dictionary_1.items():
    print(str(key) + ' : ' + value)
# values function
for value in dictionary_1.values():
    print(value)

