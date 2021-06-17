from pydantic import BaseModel
from typing import Optional


class Article(BaseModel):
    id: int
    title: str
    content: str
    author: Optional[str] = None