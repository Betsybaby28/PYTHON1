list=[]
num=int(input("enter the limit"))
for i in range(0,num):
    str=int(input("enter the data"))
    list.append(str)
print(list)
print("largest element=",max(list))
print("smallest element=",min(list))

