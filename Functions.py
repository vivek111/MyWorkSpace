def test1(**kwargs):
    print(kwargs)
    def test2():
        print("Inside test2")


def func():
    print("We are in first function")

    def func1():
        print("This is first child function")

    def func2():
        print(" This is second child function")



test2retVal=test1(name='Vivek',age=26,id='1SI13CS134')
func()

