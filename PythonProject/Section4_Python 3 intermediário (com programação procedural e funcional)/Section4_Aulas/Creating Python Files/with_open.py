# file_path = 'C:\\Users\\victo\\Atenção\\'
file_path = 'remove_unlink_rename.txt'

with open(file_path, 'w+') as file:
    print(type(file))
    file.write('Line 1\n')
    file.write('Line 2\n')
#     file.writelines(('Line 3\n', 'Line 4\n'))
#     file.seek(0, 0)
#     print(file.read())
#     print('Reading')
#     file.seek(0, 0)
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline())
#     print('READLINES')
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())

#
# print('*' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())

# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write('Line 1\n')
#     file.write('Line 2\n')
#     file.write('Atenção')

