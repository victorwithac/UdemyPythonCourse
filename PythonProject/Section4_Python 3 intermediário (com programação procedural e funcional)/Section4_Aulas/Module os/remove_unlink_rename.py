import os

file_path = 'remove_unlink_rename.txt'

with open(file_path, 'w+') as file:
    print(type(file))
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

# os.remove(file_path) # or os.unlink()

# os.rename(file_path, 'example.txt')

