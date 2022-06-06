class NewClass():
    def newfunc(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a+self.b+self.c)

    def newfunc(self,a,b):
            self.a = a
            self.b = b
            print(self.a + self.b)
obj1=NewClass()
obj1.newfunc(2,3)