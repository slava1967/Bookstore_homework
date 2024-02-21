import datetime
import itertools

from dataclasses import dataclass


@dataclass
class Book:
    new_id = itertools.count(1)
    id = next(new_id)
    title: str
    description: str
    publish_year: int
    pages_count: int
    created_at: datetime.datetime
