
# Library System

# Design a class structure for a Library system where Book has attributes title, author, and price. 
# Create a subclass EBook with additional attribute file_size. Implement methods to display details.


class Book:
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display_details(self):
        print("Book Title:", self.title)
        print("Book Author:", self.author)
        print("Book Price:", self.price)

class EBook(Book):
    def __init__(self,file_size,title,author,price):
        super().__init__(title, author, price)
        self.file_size = file_size
        Book("Python Programming","John Doe",500)
    def display_details(self):
        
        print("EBook File Size:", self.file_size)
b=Book("Python Programming","John Doe",500)
b.display_details()
e=EBook("5MB","Python Programming","John Doe",500)
e.display_details()
   
      
# Output:
# Book Title: Python Programming
# Book Author: John Doe
# Book Price: 500
# EBook File Size: 5MB