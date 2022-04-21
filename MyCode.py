def greet():
    print("Welcome to python")

def add_sub(a,b):
    sum=a+b
    diff=a-b
    return sum,diff

greet()
retValue1,retValue2=add_sub(1,2)
print(str(retValue1)+str(retValue2))