import json

class Person():
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def to_dict(self):
        return {
            'name': p1.name,
            'lastname': p1.lastname,
            'age': p1.age
        }


p1 = Person('Victor', 'Marques', 25)
person_dict = p1.to_dict()

with open('again.json', 'w') as file:
    json.dump(person_dict, file, indent=2)

with open('again.json', 'r') as file:
    person_from_json = json.load(file)

print(person_from_json)