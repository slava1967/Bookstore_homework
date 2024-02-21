class MemoryStorage:
    def __init__(self):
        self.books = []

    def get(self):
        return self.books

    def add(self, book):
        book.id = len(self.books)
        self.books.append(book)

    def delete(self, id):
        del self.books[int(id)]
