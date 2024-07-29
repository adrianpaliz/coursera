import random

file_name = input('Type the file name or the file path: ')
file = open(file_name)
file_content = file.read()
file_content_list = file_content.split('\n')
file.close()
print(random.choice(file_content_list))

