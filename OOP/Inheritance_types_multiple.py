class Father :
    def skill1 (self):
        print("Driving")

class Mother :
    def skill2 (self):
        print("Cooking")

class Child (Father , Mother):
    def skill3 (self) :
        print("Programming")

chlid_obj = Child()
chlid_obj.skill1()
chlid_obj.skill2()
chlid_obj.skill3()