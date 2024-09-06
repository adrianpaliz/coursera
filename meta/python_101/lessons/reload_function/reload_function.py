'''
import importlib
import sample

importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)
'''

import importlib
import file_changes

def changes():
    try:
        importlib.reload(file_changes)
        file_changes.print_changes()
    except:
        pass

for change in range(5):
    changes()
    input('Hit enter to reload...')

