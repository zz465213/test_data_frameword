import re
from pydantic import BaseModel, Field, field_validator


class AccountDemo(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)

    @field_validator('username')
    @classmethod
    def username_strip_and_lower(cls, v: str) -> str:
        """資料清理：移除前後空白並轉為小寫"""
        stripped_lower_username = v.strip().lower()
        if not stripped_lower_username:
            # 雖然 Field(min_length=1) 已經會檢查非空，
            # 但在這裡額外檢查可以讓錯誤訊息更明確，並確保清理後的結果仍符合要求
            raise ValueError("🔴[DEBUG]: 帳號不得為空")
        return stripped_lower_username

    @field_validator('password')
    @classmethod
    def validate_password_complexity(cls, v: str) -> str:
        """
        驗證密碼複雜度：
        - 至少包含一個大寫字母
        - 至少包含一個小寫字母
        - 至少包含一個數字
        - 至少包含一個特殊符號 (這裡定義為非字母數字字符)
        """
        # 使用正向預查 (Lookahead Assertions) 來檢查每個條件
        special_chars_pattern = r"[!@#$%^&*()_+=\[\]{}|\\:;\"'<>,.?/~`]"

        password_pattern = (
                r"^(?=.*[A-Z])"  # 至少一個大寫字母
                r"(?=.*[a-z])"  # 至少一個小寫字母
                r"(?=.*\d)"  # 至少一個數字
                r"(?=.*" + re.escape(special_chars_pattern) + r")"  # 至少一個特殊符號
        )

        if not re.fullmatch(password_pattern, v):
            raise ValueError(
                "🔴[DEBUG]: 密碼不符合複雜度要求：必須包含至少一個大寫字母、一個小寫字母、一個數字和一個特殊符號，且長度至少8碼。"
            )
        return v
