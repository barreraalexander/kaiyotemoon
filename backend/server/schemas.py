from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PoemBase(BaseModel):
    title: str
    content: str

class PoemCreate(PoemBase):
    title: str
    content: str

class Poem(PoemBase):
    id: int
    # created_at: datetime

    class Config:
        orm_mode = True

