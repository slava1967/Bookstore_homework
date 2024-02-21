from flask import Flask

from domain.book_alchemy import db
from context import Context
from views.book import bp as book_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.config["CONTEXT"] = Context()

    return app


app_run = create_app()
if __name__ == "__main__":
    app_run.run()
   