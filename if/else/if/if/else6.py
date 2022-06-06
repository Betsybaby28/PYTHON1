a=int(input("enter the age of person1"))
b=int(input("enter teh age of person2"))
c=int(input("enter the age of person3"))
if a>b and a>c:
    print("oldest age=",a)
elif b>a and b>c:
    print("oldest age=", b)
elif c>a and c>b:
    print("oldest age=",c)
elif a<b and a<c:
    print("youngest age=",a)
elif b<a and b<c:
    print("youngest age=",b)
elif c<a and c<b:
    print("youngest age=",c)