class Father :
    def skill1 (self):
        print("Driving")

# this class inherit from father class
class Mother(Father) :
    def skill2 (self):
        print("Cooking")

# This class inherit from mother class (in this time it get fathers properties also)
class Child ( Mother):
    def skill3 (self) :
        print("Programming")

child_obj = Child()
child_obj.skill1()
child_obj.skill2()
child_obj.skill3()