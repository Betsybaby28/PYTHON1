class Parent:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(self.name)
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name)
        self.age=age
    def printage(self):
        print(self.age)
obj1=Child("anu",22)
obj1.printage()
obj1.printname()
