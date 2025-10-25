# import necessary packages
from abc import ABC, abstractmethod

# create a base class
class Animal(ABC):

    # abstract method
    # should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass


# sub classes
class Human(Animal):
    def move(self):
        print("I can walk and run")


class Dog(Animal):
    def move(self):
        print("I can bark and run")


class Snake(Animal):
    def move(self):
        print("I can crawl")


# Driver code
obj1 = Human()
obj1.move()

obj2 = Dog()
obj2.move()

obj3 = Snake()
obj3.move()
