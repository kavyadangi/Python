class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def get_num_pages(self):
        return self.num_pages
    def set_num_pages(self, num_pages):
        self.num_pages = num_pages
book = Book(title="Harry Potter Series", author="J.K. Rowling", num_pages=250)
print("Title:", book.get_title())
book.set_author("J.K. Rowling")
print("Author:", book.get_author())
print("Number of Pages:", book.get_num_pages())
book.set_num_pages(260)
print("Number of Pages:", book.get_num_pages())
