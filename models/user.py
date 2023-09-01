from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, field_validator
from pydantic_core.core_schema import FieldValidationInfo


class User(BaseModel):

    id: Optional[str] = None
    first_name: str
    middle_name: Optional[str]
    last_name: str
    username: str
    email: EmailStr
    phone: str
    hashed_password: str
    is_banned: bool
    location: ...
    created_at: datetime
    updated_at: datetime


class UserIn(BaseModel):

    first_name: str
    middle_name: Optional[str]
    last_name: str
    username: str
    email: EmailStr
    phone: str
    password: constr(min_length=8)
    password2: str

    @field_validator('password2')
    @classmethod
    def password_match(cls, v, values: FieldValidationInfo, **kwargs):
        if 'password' in values.data and v != values.data['password']:
            raise ValueError('passwords don`t match')

        return v
