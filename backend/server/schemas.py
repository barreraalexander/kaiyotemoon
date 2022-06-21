from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PoemBase(BaseModel):
    name: str

class PoemCreate(PoemBase):
    pass

class Poem(PoemBase):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

