list1=[7,5,6,8]
print(len(list1))
itr=iter(list1)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

class CustomIterator:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.num<=10):
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

itr=CustomIterator()
iterable=itr.__iter__()
for i in iterable:
    print(i)