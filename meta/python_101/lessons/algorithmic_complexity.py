def find_number_log(target):
    iterations = 0
    number = range(100)
    left = 0
    right = len(number) - 1
    
    while left <= right:
        iterations += 1
        middle = (left + right) // 2
        possible_number = number[middle]

        if target == possible_number:
            print('Iterations', iterations)
            return middle
        elif target < possible_number:
            right = middle - 1
        else:
            left = middle + 1

print(find_number_log(97))

