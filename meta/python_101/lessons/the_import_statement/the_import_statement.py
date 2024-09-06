# Importing a file as a module
import sample_file

# Importing a built-in module
import random

# Impor a file and access its contents
import sys

sys.path.insert(1, r'python_101/lessons/the_import_statement/modules')
import names

print(names.names_list)

