try:
    a=int(input("enter data"))
    b=int(input("enter data"))
    print(a/b)
except ValueError:
    print("error occured")
except ZeroDivisionError:
    print("cannot divisible by zero")
else:
    print("success")
finally:
    print("the end")