# Reading files
with open('python_101/lessons/file_handling/sample_file.txt', 'r') as file:
    #print(file.readlines())
    # Because it's a list, I can assing it to a varaiable.
    #data = file.readlines()
    # When you use with open and you get as file it returns a list by default
    # We can change the for loop so that it points to the file variable
    for line in file:
        print(line)

    


