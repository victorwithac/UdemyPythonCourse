class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.upper = self.name.upper()

p1 = Person('Victor', 'Marques') #instance one
# p1.name = 'Victor'  #instance receives an attribute
# p1.lastname = 'Marques'  #instance receives an attribute
# p1.upper = p1.name.upper() #instance receives a function

# p2 = Person('João', 'Oliveira')
# p2 = Person() #instance two
# p2.name = 'João' #instance receives an attribute
# p2.lastname = 'Oliveira'  #instance receives an attribute
# p2.upper = p2.name.upper() #instance receives a function

print(p1)
print()
print(p1.upper)
print(p1.name)
print(p1.lastname)
# print()
# print(p2)
# print()
# print(p2.upper)
# print(p2.name)
# print(p2.lastname)


