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

model_1.speed_up()
