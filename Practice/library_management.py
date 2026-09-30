class LibraryItem :
    def __init__(self , item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author


class Book(LibraryItem):
    def __init__(self, item_id, title, author, genre, pages) : 
        super().__init__(item_id, title, author)
        self.genre = genre
        self.pages = pages

    def get_details(self):
        print(f"ID : {self.item_id} \n")
        print(f"Title : {self.title} \n")
        print(f"Author : {self.author} \n")
        print(f"Genre : {self.genre} \n")
        print(f"Pages : {self.pages} \n")
        print("__________________________\n")


class Magazine(LibraryItem):
    def __init__(self, item_id, title, author , issue_number, month):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number
        self.month = month

    def get_details(self):
        print(f"\nID : {self.item_id} \n")
        print(f"Title : {self.title} \n")
        print(f"Author : {self.author} \n")
        print(f"Issued No  : {self.issue_number} \n")
        print(f"Month : {self.month} \n")
        print("__________________________\n")

Book1 = Book(101, "Python Basics", "James", "Programming", 350)

Book2 = Book(102, "Clean Code", "Robert Martin", "Programming", 450)

Book3 = Book(103, "The Alchemist", "Paulo Coelho", "Fiction", 208)

print("__________________________\n")

Book1.get_details()

Book2.get_details()

Book3.get_details()

Mag1 = Magazine(201, "Tech World", "John", 45, "September")

Mag2 = Magazine(202, "Science Today", "David", 78, "August")

Mag3 = Magazine(203, "Sports Weekly", "Mike", 32, "October")

Mag1.get_details()

Mag2.get_details()

Mag3.get_details()


