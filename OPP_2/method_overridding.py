class Animal :
    def sound (self) : 
        print("Animal makes sound ")

class Dog (Animal):
    #work the sound method because of overriding(here parent and child have method with same name by calling the function with 
    # the same name it child method will be executes )
    def sound (self) : 
        print("Dog barks ")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()