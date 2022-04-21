with open('Vivek.txt','r') as fileobj:
    for line in fileobj:
        print(line,end='')
with open('Vivek.txt','r') as fileobj:
    print(fileobj.readlines())
    print(fileobj.tell())
    fileobj.seek(1) #seek(no of bytes to be moved, reference pos(0-start,1-cur,2-end))
    print(fileobj.tell())

import os
#os.rmdir('VIVEK')
print(os.getcwd())