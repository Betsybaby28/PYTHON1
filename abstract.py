from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
       print("walking")

class Dog(Animal):
    def move(self):
        print("running")
h=Human()
h.move()
