from dataclasses import dataclass


@dataclass
class AccountDemo:
    username: str
    password: str

    def __post_init__(self):
        self.username = self.username.strip().lower()

        # 驗證 username 不為空
        if not self.username:
            raise ValueError("帳號不得為空")

        # 驗證 password 不為空 (在雜湊前檢查)
        if not self.password:
            raise ValueError("密碼不得為空")
        if len(self.password) < 8:
            raise ValueError("密碼需要大於8碼")
