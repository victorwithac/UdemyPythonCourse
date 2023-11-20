class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

        @property
        def tool(self):
            return self._tool

        @tool.setter
        def tool(self, tool):
            self._tool = tool

class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing'


writer = Writer('Victor')
pen = WritingTool('Blue pen')
writer.tool = pen
print(pen.write())
print(writer.tool.write())