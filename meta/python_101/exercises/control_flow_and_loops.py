numbers_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for index, number in enumerate(numbers_list):
    count += 1
    if number == 36:
        print('Number found at position:', index)
        break

print('The count is', count)    

