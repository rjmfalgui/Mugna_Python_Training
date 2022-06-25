class Library:
    books = []

    def __init__(self, name):
        self.name = name

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        self.books.pop(book)

library_1 = Library(name="Public Library")
library_2 = Library(name="Private Library")

library_1.add_books("Book 3")
library_1.add_books("Book 5")
library_1.add_books("Book 63")
library_1.add_books("Book 75")
library_1.add_books("Book 43")
library_1.add_books("Book 55") 

print(library_1.books)