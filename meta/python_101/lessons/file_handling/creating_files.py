# Creating files
# We use 'w' for remplace or 'a' to append to the current file
with open('python_101/lessons/file_handling/new_file.txt', 'a') as file:
    file.writelines(['\nThis is a new file created!', '\nThis is another line to be added'])

