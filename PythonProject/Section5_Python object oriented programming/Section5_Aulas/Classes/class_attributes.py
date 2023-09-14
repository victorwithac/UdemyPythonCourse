class Person:
    current_year = 2023
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age



p1 = Person('Levi', 23)
p2 = Person('Helena', 12)
p3 = Person('Victor', 26)

print(Person.current_year)
print(p1.get_birth_year())
print(p2.get_birth_year())
print(p3.get_birth_year())
