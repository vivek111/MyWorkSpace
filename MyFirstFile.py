a=10
b=20
c=a
print(a)
def printval():
    print("Inside function")
    global a
    a=20
    print(a)
print(id(a),id(b),id(c), sep='   ')
printval()
print(a)

a,b,c,d,e=1,2,3,4,5
print(a,b,c,d,e,sep='',end='\n')
a=5+7j
print(isinstance(a,complex))

list1=list()
list1.insert(0,12)
list1.insert(1,"Hello")
list1.insert(3,"Append")

list1.append("Append")
print(list1)

list2=list1.copy()
print(list1.count('Append'))
print(list2)
list2.remove('Append')
print(list2)
table=int(input('Enter the the table'))
i=1

while (i<=10):
    print(table,' x'+str(i)+'=',int(table*i))
    i+=1