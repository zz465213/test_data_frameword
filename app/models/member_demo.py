from dataclasses import dataclass
import re


@dataclass
class MemberDemo:
    username: str
    email: str
    phone: str
    age: int

    def __post_init__(self):
        """資料清理和基本驗證"""
        # 資料清理
        self.username = self.username.strip()
        self.email = self.email.strip().lower()
        self.phone = self.phone.strip()

        # 基本驗證 - 只做必要的資料完整性檢查
        if not self.username:
            raise ValueError("使用者名稱不得為空")

        if not self.email:
            raise ValueError("Email 不得為空")

        if not self.phone:
            raise ValueError("電話號碼不得為空")

        if not isinstance(self.age, int):
            raise ValueError("年齡必須是整數")

    def validate_for_creation(self):
        """創建時的完整驗證"""
        # Email 格式驗證
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError(f"不合理的 Email 格式: {self.email}")

        # 台灣手機號碼驗證
        if not re.fullmatch(r"^09\d{8}$", self.phone):
            raise ValueError(f"不合理的台灣手機格式: {self.phone}. 必須為 09 開頭且為 10 碼")

        # 年齡範圍驗證
        if self.age <= 0 or self.age > 150:
            raise ValueError("年齡必須在 1-150 之間")

        # 使用者名稱長度驗證
        if len(self.username) < 3 or len(self.username) > 50:
            raise ValueError("使用者名稱長度必須在 3-50 字元之間")

    def to_dict(self):
        """轉換為字典格式，用於 JSON 回應"""
        return {
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'age': self.age
        }