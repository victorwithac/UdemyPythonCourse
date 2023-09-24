class Person:
    current_year = 2023
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age

p1 = Person('Victor', 25)
print(p1)
# del p1.name
p1.name = 'Levi'
# print(p1.__dict__)
p1.__dict__['lastname'] = 'Marques'
del p1.__dict__['age']
print(vars(p1))
print(p1.lastname)

