import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age
        }


p1 = Person('Victor', 25)
person_dict = p1.to_dict()




with  open('class_in_json.json', 'w') as file:
    json.dump(person_dict, file, indent=2)

with open('class_in_json.json', 'r') as file:
    person_from_json = json.load(file)
    person_2 = Person(person_from_json['name'], person_dict['age'])

print(person_2.name, person_2.age) #object from json
print(person_from_json['name']) #dictionary
print(p1.name) #Instance of my class
