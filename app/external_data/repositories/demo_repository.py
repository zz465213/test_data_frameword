import logging
from app.adapters.db_factory import DBFactory
from app.utils.file_tool import read_yaml
from app.models.member_demo import MemberDemo
from app.models.account_demo import AccountDemo
from configs.common_paths import CONFIGS_FILE
from typing import List, Optional


class DemoRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.mysql = DBFactory().get_mysql(
            host=read_yaml(CONFIGS_FILE)["mysql"]["host"],
            user=read_yaml(CONFIGS_FILE)["mysql"]["user"],
            password=read_yaml(CONFIGS_FILE)["mysql"]["password"],
            database=read_yaml(CONFIGS_FILE)["mysql"]["database"]
        )

    def create_member(self, member_demo: MemberDemo, params: tuple) -> MemberDemo:
        sql = "INSERT INTO member (username, email, phone, age) VALUES (%s, %s, %s, %s)"
        try:
            self.mysql.insert(sql, params)
            logging.info(f"🟢 成員資料建立成功，使用者名稱: {member_demo.username}, Email: {member_demo.email},"
                         f" 電話: {member_demo.phone}, 年齡:{member_demo.age}")
        except Exception as e:
            logging.error(f"🔴 建立成員資料發生非預期錯誤, {e}")
            raise

    def create_account(self, account_demo: AccountDemo) -> MemberDemo:
        sql = "INSERT INTO member (username, password)"
        f"VALUES ({account_demo.username}, {account_demo.password});"
        try:
            self.mysql.insert(sql)
            logging.info(f"🟢 成員資料建立成功，使用者名稱: {account_demo.username}, 密碼: {account_demo.password}")
        except Exception as e:
            logging.error(f"🔴 建立帳號資料發生非預期錯誤, {e}")
            raise

    def get_member_all_data(self) -> List[MemberDemo]:
        sql = "SELECT * FROM member"
        try:
            return self.mysql.fetch_all(sql)
        except Exception as e:
            logging.error(f"🔴 搜尋成員資料發生非預期錯誤, {e}")
            raise

    def get_member_by_phone(self, phone_no: str) -> Optional[MemberDemo]:
        sql = f"SELECT * FROM member WHERE phone = {phone_no}"
        try:
            return self.mysql.fetch_all(sql)
        except Exception as e:
            logging.error(f"🔴 使用 {phone_no} 搜尋成員資料發生非預期錯誤, {e}")
            raise


if __name__ == "__main__":
    pass
