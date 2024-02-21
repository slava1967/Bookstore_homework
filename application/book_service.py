class BookService:
    def __init__(self, storage):
        self.storage = storage

    def get(self):
        return self.storage.get()

    def add(self, book):
        return self.storage.add(book)

    def delete(self, id):
        self.storage.delete(id)
