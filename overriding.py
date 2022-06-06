class Parent:
    def printdata(self):
        print("inside parent")
class Child(Parent):
    def printdata(self):
        super().printdata()
        print("inside child")
obj1=Child()
obj1.printdata()