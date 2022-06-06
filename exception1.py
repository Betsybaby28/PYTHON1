try:
    f_obj=open("read.txt",'r')
    data = f_obj.read()
except FileNotFoundError:
    print("file is not existed")
else:
    print("success")
finally:
    print("the end")