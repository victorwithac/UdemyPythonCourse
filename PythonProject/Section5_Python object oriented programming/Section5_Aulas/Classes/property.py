# @property - is a getter in a pythonic way
# getter - is a method to obtain an attribute
# pythonic - is a python way of doing things
# Generally used in the following situations:
# like a getter
# to avoid breaking client code
# to enable setter
# to perform actions when obtaining an attribute
# Cliente Code - it's a code that uses your code


class Pen:
    def __init__(self, color):
        self.color = color
wor