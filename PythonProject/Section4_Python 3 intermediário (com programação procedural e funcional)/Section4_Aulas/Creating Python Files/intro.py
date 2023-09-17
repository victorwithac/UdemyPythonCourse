# file_path = 'C:\\Users\\victo\\Atenção\\'
file_path = 'intro.txt'
print(file_path)

# file = open(file_path, 'w')
#
# file.close()

#The difference between the code above and the code below is using
#using the 'with' the file will be close by itself

with open(file_path, 'w') as file:
    ...
