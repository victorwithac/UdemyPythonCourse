import json

FILE_PATH = 'again.json'

class Person():
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    # def to_dict(self):
    #     return {
    #         'name': p1.name,
    #         'lastname': p1.lastname,
    #         'age': p1.age
    #     }


p1 = Person('Victor', 'Santos', 25)
p2 = Person('Marcos', 'Santos', 25)
p3 = Person('Andre', 'Santos', 25)
person_dict = [p1.__dict__, p2.__dict__, p3.__dict__]

# print(person_dict)

def do_dump():
    with open(FILE_PATH, 'w') as file:
        json.dump(person_dict, file, indent=2)

print(__name__)

# with open('again.json', 'r') as file:
#     person_from_json = json.load(file)
#     # for persons in person_from_json:
        # print(persons)



