class book:
    def __init__(self):
        self.title=input("Enter title of book")
        self.author=input("Enter author name")
    def display(self):
        if hasattr(self,'publisher'):
            print(self.title,"Written by",self.author,"is published",self.publisher)
             
        else:
            print("Unknown publisher")
b=book()
b.display()
setattr(b,'publisher','Penguin books')
b.display()
