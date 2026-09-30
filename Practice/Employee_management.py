
class Employee :
    def __init__(self ,emp_id , name , basic_salary) :
        self.emp_id = emp_id
        self.name = name
        self.salary= basic_salary


class Developer(Employee):
    def __init__(self ,emp_id , name , basic_salary , programming_lang , experience):
        super().__init__(emp_id , name , basic_salary )
        self.programming_lang = programming_lang
        self.experience = experience

    def get_details(self):
         print(f" id : {self.emp_id} \n\n name : {self.name} \n\n salary : {self.salary+5000} \n\n language : {self.programming_lang} \n\n experience : {self.experience} years \n\n_________________________\n")

class Manager(Employee):
    def __init__(self ,emp_id , name , basic_salary , team_size ,department ):
        super().__init__(emp_id , name , basic_salary )
        self.team_size = team_size
        self.department = department

    def get_details(self):
        print(f" id : {self.emp_id} \n\n name : {self.name} \n\n salary : {self.salary+5000} \n\n team_size : {self.team_size} members \n\n department : {self.department} \n\n_________________________\n")

print("_________________________ \n")

dev1 = Developer(101, "Arun", 35000, "Python", 2)
dev1.get_details()

dev2 = Developer(102, "Rahul", 42000, "JavaScript", 3)
dev2.get_details()

man1 = Manager(201, "Suresh", 60000, 5, "Development")
man2 = Manager(202, "Anjali", 70000, 8, "Marketing")

man1.get_details()
man2.get_details()
