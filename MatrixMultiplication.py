from numpy import *
def multiply(m1,m2):
    if(m1.shape[1]!=m2.shape[0]):
        print('Matrix multiplication not possible')
        return False
    else:
        m3=list()
        for i in range(0,m1.shape[0]):
            row=list()
            for j in range(0,m1.shape[1]):
                sum=0
                for k in range(0,m2.shape[1]):
                    sum=sum+(m1[i][k]*m2[k][j])
                row.append(sum)
            m3.append(row)
            del row
        matrix3=array(m3)
        print(matrix3)
        return True

def getmatrix():
    print('Enter the details of the first matrix')
    row1 = int(input(('Enter the rows')))
    column1 = int(input(('Enter the columns')))
    print('Enter the details')
    matrix1=list()
    for i in range(0,row1):
        row=list()
        for j in range(0,column1):
            row.append(int(input('row {0}, column {1}'.format(i+1,j+1))))
        matrix1.append(row)
        del row
    print(matrix1)

    print('Enter the details of the second matrix')
    row2 = int(input(('Enter the rows')))
    column2 = int(input(('Enter the columns')))
    print('Enter the details')
    matrix2 = list()
    for i in range(0, row2):
        row = list()
        for j in range(0, column2):
            row.append(int(input('row {0}, column {1}'.format(i + 1, j + 1))))
        matrix2.append(row)
        del row
    print(matrix2)
    m1=array(matrix1)
    m2=array(matrix2)
    return m1,m2
m1,m2,=getmatrix()
print(m1.shape,m2.shape)
returnValue=multiply(m1,m2)



