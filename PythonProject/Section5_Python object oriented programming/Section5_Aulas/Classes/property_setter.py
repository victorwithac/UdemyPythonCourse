class Pen:
    def __init__(self, color):
        self._color = color #whenever there is an underline, it means it should not be modified


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value == 'Red':
            raise ValueError('Don`t use this color')
        self._color = value


# pen = Pen('Blue')
pen = Pen('Black')
# cap = Pen('Green')
#
# print(cap.color)
# print(pen.color)
pen.color = 'Yellow'

print(pen.color)