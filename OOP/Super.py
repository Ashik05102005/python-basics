class Animal :
    def __init__(self,name):
        self.name = name

class Dog (Animal) :
    def __init__(self,name , breed) :
        super().__init__(name)
        self.breed = breed

dog_obj = Dog("Tom" , "Lab")
print(dog_obj.name)
print(dog_obj.breed)