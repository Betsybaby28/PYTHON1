str=input("enter the string")
v=0
c=0
d=0
w=0
vowels='aeiou'
for i in str:
    if i in vowels:
        v=v+1
print("vowels=",v)
for i in str:
    if i not in vowels:
        c=c+1
print("consonants=",c)
for i in str:
    if(i.isdigit()):
        d=d+1
print("digits=",d)
for i in str:
    if(i.isspace()):
        w=w+1
print("whitespace=",w)

