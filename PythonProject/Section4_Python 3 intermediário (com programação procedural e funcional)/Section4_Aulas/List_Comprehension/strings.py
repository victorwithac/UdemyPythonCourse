string = 'Otavio Miranda'
new_string = [
    string[index:index + 2]
    for index in range(len(string))
]
print(new_string)

