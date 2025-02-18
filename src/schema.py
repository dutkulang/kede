from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    body: Optional[str] = None
    published : bool = False