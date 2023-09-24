#Instances methods in Python classes

class Car:
    def __init__(self, model_name):
        self.name = model_name

    def speed_up(self):
        print(f'{self.name} is accelerating ')



model_1 = Car('civic')
print(model_1.name)
model_2 = Car('city')
print(model_2.name)
print()
model_1.speed_up()
model_2.speed_up()
print()#Or
Car.speed_up(model_1)
Car.speed_up(model_2)
