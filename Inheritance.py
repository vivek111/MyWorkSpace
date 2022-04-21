class A:
    aVar='A'
    def __init__(self):
        print('In A')
    def feature1(self):
        print('In class A')
class B:
    bVar='B'
    def __init__(self):
        print('In B')
    def feature1(self):
        print('In class B')
class C(B,A):
    cVar='C'

    def __init__(self):
        print('In C')
        super().__init__()
        super().__init__()
    def feature3(self):
        print('In class C')
        super().feature1()

cClass=C()
cClass.feature3()