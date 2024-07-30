def find_number(number_to_search):
    count = 0
    for number in range(100):
        if number == number_to_search:
            print('Total iterations: ', count)
            return number
        count += 1

find_number(97)

