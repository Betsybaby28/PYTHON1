class Person:
    def printdata(self,name=None):
        if name is not None:
            print("hello"+name)
        else:
            print("hai")
obj1=Person()
obj1.printdata()
obj1.printdata("tom")