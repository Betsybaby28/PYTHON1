def find_len(list1):
    length=len(list1)
    list1.sort()
    print("largest element",list1(length-1))
    print("second largest",list1(length-2))
    print("smallest",list1[0])
    print("second smallest",list1[1])
list1=[2,5,8,3,6,5]
largest=find_len(list1)
