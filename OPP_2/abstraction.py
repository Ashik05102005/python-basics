from abc import ABC , abstractmethod

class Animal (ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print(" dog barks ")
        
class Cat(Animal):
    def sound(self):
        print(" cat meow ")
    
cat = Cat()
dog = Dog()

dog.sound()
cat.sound()