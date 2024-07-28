# Reading files
with open('python_101/lessons/file_handling/sample_file.txt', 'r') as file:
    #print(file.readlines())
    # Because it's a list, I can assing it to a varaiable.
    data = file.readlines()
    for line in data:
        print(line)

    


