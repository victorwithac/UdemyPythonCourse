#Class scope and class methods

class Animal:
    # name = 'Lion'
    def __init__(self, name):
        self.name = name
        # variable_init_scope = 'Value'
        # print(variable_init_scope)
    def eating(self, food):
        return f'{self.name} is eating {food}'
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)

lion = Animal('Lion')
print(lion.name)
print()
print(lion.execute('banana'))
