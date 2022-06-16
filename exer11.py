class Library:

    books = []

    def __init__(self, name):
        self.name = name
    pass

    def addBooks(self, book):
        self.books.append(book)

    def removeBooks(self, book):
        self.books.pop(book)

library_1 = Library(name="Public Library")
library_2 = Library(name="Private Library")

library_1.addBooks("Book 3")
library_1.addBooks("Book 5")
library_1.addBooks("Book 63")
library_1.addBooks("Book 75")
library_1.addBooks("Book 43")
library_1.addBooks("Book 55") 

print(library_1.books)