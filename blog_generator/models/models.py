from datetime import date

from pydantic import BaseModel, HttpUrl, conlist


class Link(BaseModel):
    title: str
    authors: list[str] = []
    tags: conlist(str, min_items=1)
    link: HttpUrl
    date: date
