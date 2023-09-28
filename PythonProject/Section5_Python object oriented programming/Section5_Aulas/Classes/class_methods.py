#Class methods and factories



class Person:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def class_method(cls):
        print('hey')

    @classmethod
    def create_with_50_years(cls, name):
        return cls(name, 50)

    @classmethod
    def create_with_50_years(cls, name):
        return cls(name, 50)

    @classmethod
    def create_without_name(cls, age):
        return cls('Anonimous', age)




# p1 = Person('Victor', 25)
p2 = Person.create_with_50_years('Helena')
print(p2.name, p2.age)


p3 = Person('Anonimous', 25)
p4 = Person.create_without_name(25)


print(p3.name, p3.age)
print(p4.name, p4.age)
# Person.class_method()

# print(Person.year)
# Person.class_method()