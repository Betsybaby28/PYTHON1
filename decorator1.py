import time
def hello_decor(func):
    def inner(*a):
        start=time.time()
        time.sleep(1)
        func(*a)
        print(time.time()-start)
    return inner
@hello_decor
def newfunc(a,b):
    print(a)
    print(b)
    print(a+b)
newfunc(299,300)

