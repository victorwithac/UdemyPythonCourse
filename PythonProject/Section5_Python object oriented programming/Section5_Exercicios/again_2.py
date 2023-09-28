import json

from again import FILE_PATH, Person


with open(FILE_PATH, 'r') as file:
    persons_from_json = json.load(file)
    p1 = Person(**persons_from_json[0])
    p2 = Person(**persons_from_json[1])
    p3 = Person(**persons_from_json[2])


    print(p1.name, p1.age)

print(__name__)

# def my_function(**kwargs):
#     for chave,valor in kwargs.items():
#         print(chave, valor)
# #
# #
# my_function('Victor', 'Marques', 'Santos')