# File handling
file = open('python_101/lessons/file_handling/local_file.txt', mode = 'r')

data = file.readline()

print(data)

file.close()

