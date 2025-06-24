import re
from pydantic import BaseModel, EmailStr, Field, field_validator


class MemberDemo(BaseModel):
    username: str = Field(min_length=6, max_length=20)
    email: EmailStr
    phone: str
    age: int = Field(gt=0, lt=151)

    @field_validator('username')
    @classmethod
    def username_strip(cls, v: str) -> str:
        return v.strip()

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        stripped_phone = v.strip()
        if not re.fullmatch(r"^09\d{8}$", stripped_phone):
            raise ValueError(f"🔴 不合理的台灣手機格式: {stripped_phone}. 必須為 09 開頭且為 10 碼")
        return stripped_phone


if __name__ == "__main__":
    pass
