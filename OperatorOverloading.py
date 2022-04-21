class Polymorphism:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,obj2):
        self.a+=obj2.a
        self.b+=obj2.b
        return self

obj1=Polymorphism(12,14)
obj2=Polymorphism(20,45)
obj3=(obj1+obj2)
print(obj3.a)

