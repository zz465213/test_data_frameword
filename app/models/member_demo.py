import re
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from app.exceptions.custom_exception import *

username_min = 6
username_max = 20
age_min = 0
age_max = 150


class MemberDemo(BaseModel):
    username: str = Field(min_length=username_min, max_length=username_max)
    email: EmailStr
    phone: str
    age: int = Field(gt=age_min, lt=age_max)

    @model_validator(mode='after')
    def validate_all_fields(self) -> 'MemberDemo':
        """
        驗證失敗會拋出 ValidationError。
        """
        return self

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        phone_no = v.strip()
        if not re.fullmatch(r"^09\d{8}$", phone_no):
            raise InvalidPhoneFormatException(phone_no=phone_no)
        return phone_no

    @field_validator('username')
    @classmethod
    def validate_username(cls, v: str) -> str:
        username = v.strip()
        if len(username) < username_min:
            raise ValueBelowMinError(current_no=len(username), min_no=username_min)
        elif len(username) > username_max:
            raise ValueAboveMaxError(current_no=len(username), max_no=username_max)
        return username

    @field_validator('age')
    @classmethod
    def validate_age(cls, age: int) -> int:
        if age < age_min:
            raise ValueBelowMinError(current_no=age, min_no=username_min)
        elif age > age_max:
            raise ValueAboveMaxError(current_no=age, max_no=username_max)
        return age


if __name__ == "__main__":
    pass
