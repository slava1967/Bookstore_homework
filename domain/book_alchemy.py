from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@dataclass
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(unique=False)
    publish_year: Mapped[int] = mapped_column(unique=False)
    pages_count: Mapped[int] = mapped_column(unique=False)
    created_at: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"Book (title={self.title})"
