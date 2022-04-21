class Student:
    university='SIT'
    def __init__(self,rollNum,name):
        self.rollNum=rollNum
        self.name=name
        self.lap=self.Laptop()
    def show(self):
        print(self.name+self.rollNum)
    class Laptop:
        def __init__(self):
            self.cpu='i5'
            self.ram=8

        @staticmethod
        def show(self):
            print(self.cpu+str(self.ram))
student1=Student(1,'Vivek')
student1.lap=Student.Laptop()
Student.Laptop.show(student1.lap)
print(Student.university)
print(student1.university)