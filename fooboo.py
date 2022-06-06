for i in range(1,101):
    if ((i%3==0) and (i%5==0)):
        print("fooboo")
    elif i%3==0:
        print("foo")
    elif i%5==0:
        print("boo")
    else:
        print(i)