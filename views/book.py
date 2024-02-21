import dataclasses
import json

from flask import current_app, Blueprint, request

from context import get_context
from domain.book_alchemy import Book

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)

    return json.dumps([dataclasses.asdict(b) for b in ctx.book_service.get()])


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)

    book = Book(**request.json)
    ctx.book_service.add(book)
    return {}


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return {}
