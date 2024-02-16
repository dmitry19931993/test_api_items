from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr, validator, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime



class UserIn(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    name: str
    email: EmailStr
    password: str
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("password don't match")
        return v