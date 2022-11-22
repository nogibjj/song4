from pydantic import BaseModel, EmailStr
from typing import Optional


class RequestEmailSch(BaseModel):
    user_email: EmailStr
    title: str
    content: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_email": "song.oh@outlook.com",
                "title": "Hello",
                "content": "Happy Thanksgiving!",
            }
        }

