from flask import request

from domain.book_alchemy import db, Book


class SQLiteStorage:

    @staticmethod
    def get():
        books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
        return books

    @staticmethod
    def add(book):
        if request.method == "POST":
            db.session.add(book)
            db.session.commit()

    @staticmethod
    def delete(id):
        book = db.get_or_404(Book, id)
        db.session.delete(book)
        db.session.commit()
