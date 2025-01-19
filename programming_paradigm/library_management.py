class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False


class Library(Book):
    def __init__(self):
        self.books = []
        self.original = []

    def add_book(self, book):
        self.books.append(book)
        self.original.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.__is_checked_out = True
                return book

    def return_book(self, title):
        for book in self.original:
            if book.title == title:
                self.books.append(book)
                self.__is_checked_out = False

    def list_available_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")
    

    