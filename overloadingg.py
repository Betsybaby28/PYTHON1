def sum(a,b):
    return a+b
def sum(a,b,c=0):
    return a+b+c
def sum(*args):
    total=0
    for i in args:
        total+=i
    return total
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,5))


