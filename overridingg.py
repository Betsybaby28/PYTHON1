class Animal:
    def move(self):
        print("i'm moving")
class Human(Animal):
    def move(self):
        print("i'm waking")
h=Animal()
h.move()