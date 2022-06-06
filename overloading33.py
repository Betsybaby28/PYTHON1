class NewClass():
   def sum(self,a,b):
       return a+b
   def sum(self,a,b,c=0):
       return a+b+c
   def sum(self,*args):
       total=0
       for i in args:
           total+=i
       return total
obj1=NewClass()
print(obj1.sum(1,2))
print(obj1.sum(1,2,3))
print(obj1.sum(1,2,3,4,5))