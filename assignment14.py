list1=range(31)
newlist=list1[1:6]+list1[25:31]
i=newlist*newlist
newlist.append(i)
print(newlist)