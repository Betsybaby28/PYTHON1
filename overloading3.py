class Shape:
    def printdata(self,l,b=None):
        if b is not None:
            print("rectangle")
            print(l*b)
        else:
            print("square")
            print(l*l)
obj1=Shape()
obj1.printdata(2,6)

