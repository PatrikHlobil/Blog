from datetime import date

from pydantic import BaseModel, HttpUrl


class Link(BaseModel):
    title: str
    authors: list[str] | None
    tags: list[str] | None
    link: HttpUrl
    date: date


class Config(BaseModel):
    links: list[Link]
