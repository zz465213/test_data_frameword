import logging
from app.adapters.db_factory import DBFactory
from app.models.member_demo import MemberDemo
from typing import List, Optional


class DemoRepository:
    def __init__(self, db_config: dict):
        self.logger = logging.getLogger(__name__)
        self.mysql = DBFactory().get_mysql(**db_config)

    def create_member(self, member_demo: MemberDemo) -> int:
        """
        創建成員資料
        Returns: 新建立的成員 ID
        """
        sql = "INSERT INTO member (username, email, phone, age) VALUES (%s, %s, %s, %s)"
        params = (member_demo.username, member_demo.email, member_demo.phone, member_demo.age)

        try:
            result = self.mysql.insert(sql, params)
            member_id = result.lastrowid if hasattr(result, 'lastrowid') else None

            self.logger.info(f"🟢 成員資料建立成功，ID: {member_id}, 使用者名稱: {member_demo.username}")
            return member_id

        except Exception as e:
            self.logger.error(f"🔴 建立成員資料發生錯誤: {e}")
            raise

    def get_member_all_data(self) -> List[MemberDemo]:
        sql = "SELECT username, email, phone, age FROM member"
        try:
            return self.mysql.fetch_all(sql)
        except Exception as e:
            logging.error(f"🔴 搜尋成員資料發生非預期錯誤, {e}")
            raise

    def get_member_by_phone(self, phone_no: str) -> Optional[MemberDemo]:
        sql = "SELECT username, email, phone, age FROM member WHERE phone = %s"
        try:
            return self.mysql.fetch_all(sql, (phone_no,))
        except Exception as e:
            logging.error(f"🔴 使用 {phone_no} 搜尋成員資料發生非預期錯誤, {e}")
            raise


if __name__ == "__main__":
    pass
