class X:
    def print(self,*args):
        sum=0
        for i in args:
            sum=sum+i
        print(sum)
class Y(X):
    def print(self,*args):
        sum=1
        print('Method Overriding')
        for i in args:
            sum=sum*i
        print(sum)
    pass
xobj=Y()
xobj.print(1,2,3,5,6,7)