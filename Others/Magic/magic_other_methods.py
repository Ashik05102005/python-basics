class Team :
    def __init__(self,members):
        self.members =  members

    def __len__(self):
        return len(self.members)

    def __getitem__(self, key):
        return self.members[key]

    def __call__(self, *args, **kwds):
        print("we can call the object like function")
        

team = Team(["Ashik" , "Arun" , "Rahul"])
print(len(team))
print(team[0])
team()
