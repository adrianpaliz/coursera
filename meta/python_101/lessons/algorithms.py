# Algorithm for a Palindrome

def is_palindrome(string):
    start_index = 0
    end_index = len(string) - 1

    for letter in string:
        if string[start_index] != string[end_index]:
            return False
    return True

print(is_palindrome('racecar'))
