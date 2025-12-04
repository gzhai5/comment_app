from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CommentModel(BaseModel):
    id: str = Field(...)
    author: str = Field(...)
    text: str = Field(...)
    date: datetime = Field(default_factory=datetime.utcnow)
    likes: int = Field(default=0)
    image: str = Field(default="")

class UpdateCommentModel(BaseModel):
    author: Optional[str] = None
    text: Optional[str] = None
    date: Optional[datetime] = None
    likes: Optional[int] = None
    image: Optional[str] = None