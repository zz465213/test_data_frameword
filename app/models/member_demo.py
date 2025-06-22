from dataclasses import dataclass
import re


@dataclass
class MemberDemo:
    username: str
    email: str
    phone: str
    age: int

    # def __post_init__(self):
    #     self.username = self.username.strip().lower()
    #     self.email = self.email.strip().lower()
    #
    #     # 驗證 username 不為空
    #     if not self.username:
    #         raise ValueError("使用者名稱不得為空")
    #
    #     # 驗證 email 格式
    #     if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email):
    #         raise ValueError(f"不合理的 Email 格式: {self.email}")
    #
    #     # 驗證台灣手機號碼通常為 09 開頭且共 10 位
    #     if not re.fullmatch(r"^09\d{8}$", self.phone):
    #         raise ValueError(
    #             f"不合理的台灣手機格式: {self.phone}. 必續為 09 開頭且為 10 碼")
    #
    #     # 驗證 age 必須是正整數
    #     if not isinstance(self.age, int) or self.age <= 0:
    #         raise ValueError("年齡必須是正整數")
