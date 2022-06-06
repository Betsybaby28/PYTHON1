def hello_decor(func):
    def inner():
        print("before function")
        func()
        print("after function")
    return inner
@hello_decor
def newfunc():
    print("inside function")
newfunc()