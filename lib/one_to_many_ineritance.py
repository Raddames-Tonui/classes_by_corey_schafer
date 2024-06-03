class Book:
    all_books = []
    def __init__(self, title) -> None:
        self.title = title
    
    @classmethod
    def count_books(self):
        return len(self.all_books)

class Library:
    def __init__(self) -> None:
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

book1 = Book("Hello Python")
book2 = Book("Java Into")
book3 = Book("python intro")
print(book1)
lib1 = Library()
lib1.add_book(book1)
lib1.add_book(book2)
lib1.add_book(book3)

for book in  lib1.books:
    print(book.title)

