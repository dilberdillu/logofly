from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import datetime


class CreateLogo(BaseModel):
    prompt: str
    image: bytes

    class Config:
        orm_mode = True

class ShowLogo(BaseModel):
    prompt: str
    image: bytes
    created_at: datetime

    class Config:
        from_attributes = True