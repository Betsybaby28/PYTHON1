d=0
l=0
str=input("enter the sentence")
for i in str:
    if(i.isdigit()):
        d=d+1
print("digits=",d)
for i in str:
    if(i.isalpha()):
       l=l+1
print("letters=",l)

