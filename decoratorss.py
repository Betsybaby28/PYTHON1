def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("i am ordinary")
obj1=ordinary()