x=5
x='Vivek'
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')
class MyEditor:
    def execute(self):
        print('Play Songs')
        print('Play dialogues')
class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditor()
laptop=Laptop()
laptop.code(ide)
