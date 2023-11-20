#Encapsulation
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'this is public' #can be used in anywhere
        self._protected = 'this is protected' #can only be used within the classes and sub classes
        self.__private = 'this is private' #can only be used within the class

    def public_method(self):
        print(self.__private)
        return 'public_method'

    def _protected_method(self):
        print('_protected_method')
        return '_protected_method'

    def __private_method(self):
        print('__private_method')
        return '__private_method'

f = Foo()
print(f.public_method())
# print(f._Foo__private_method()) #This should not be done outside of class

