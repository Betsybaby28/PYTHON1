class Parent1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def nameage(self):
        print(self.name)
        print(self.age)
class Parent2:
    def __init__(self,address):
        self.address=address
    def printaddress(self):
        print(self.address)
class Child(Parent1,Parent2):
    def __init__(self,name,age,address,phone):
        Parent1.__init__(self,name,age)
        Parent2.__init__(self,address)
        self.phone=phone
    def printphone(self):
        print(self.phone)
obj1=Child("anu",22,"ekm",3333)
obj1.nameage()
obj1.printaddress()
obj1.printphone()

