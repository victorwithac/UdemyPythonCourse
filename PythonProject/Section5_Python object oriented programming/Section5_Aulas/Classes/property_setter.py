class Pen:
    def __init__(self, color):
        # self.paint_color = color
        self.color = color
        #whenever there is an underline, it means it should not be modified


    # @property
    # def color(self):
    #     print('Property')
    #     return self.paint_color

# def show_pen(pen):
#     return pen.color

    def get_color(self):
        return self.color



pen = Pen('Black')
var = pen.get_color()
print(var)

# pen = Pen('Blue')

# cap = Pen('Green')
#
# print(pen.color)
# print(cap.color)
# print(pen.color)

# show_pen(pen)

