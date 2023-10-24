class Pen:
    def __init__(self, color):
        self.paint_color = color
        self._color = self.paint_color #whenever there is an underline, it means it should not be modified


        @property
        def color(self):
            print('Property')
            return self.paint_color

