import traceback
import mysql.connector
from app.adapters.db_factory import DBFactory
from app.models.member_demo import MemberDemo
from app.exceptions.database_exception import *
from typing import List, Optional


class DemoRepository:
    def __init__(self):
        self.mysql = DBFactory().get_mysql()

    def create_member(self, member_demo: MemberDemo) -> int:
        """
        創建成員資料
        Returns: 新建立的成員 ID
        """
        try:
            sql = "INSERT INTO member (username, email, phone, age) VALUES (%s, %s, %s, %s)"
            params = (member_demo.username, member_demo.email, member_demo.phone, member_demo.age)
            result = self.mysql.insert(sql, params)
            member_id = result.lastrowid if hasattr(result, 'lastrowid') else None
            return member_id
        except mysql.connector.OperationalError as e:
            raise DatabaseInsertException(f"🔴[DEBUG]: {__name__} 建置時發生操作問題: {e}\n"
                                          f"--- 打印錯誤追溯 ---\n"
                                          f"{traceback.format_exc()}")
        except Exception:
            raise

    def get_member_all_data(self) -> List[MemberDemo]:
        try:
            sql = "SELECT username, email, phone, age FROM member"
            member_data = self.mysql.fetch_all(sql)
            if member_data is None:
                raise DataNotFoundError(f"🔴[DEBUG]: {__name__} 查無資料")
            return member_data
        except mysql.connector.OperationalError as e:
            raise DatabaseFetchFailException(f"🔴[DEBUG]: {__name__} 搜尋資料時發生操作問題: {e}\n"
                                             f"--- 打印錯誤追溯 ---\n"
                                             f"{traceback.format_exc()}")
        except Exception:
            raise

    def get_member_by_phone(self, phone_no: str) -> Optional[MemberDemo]:
        try:
            sql = "SELECT username, email, phone, age FROM member WHERE phone = %s"
            return self.mysql.fetch_all(sql, (phone_no,))
        except mysql.connector.OperationalError as e:
            raise DatabaseFetchFailException(f"🔴[DEBUG]: {__name__} 搜尋Phone={phone_no}時發生操作問題: {e}\n"
                                             f"--- 打印錯誤追溯 ---\n"
                                             f"{traceback.format_exc()}")
        except Exception:
            raise


if __name__ == "__main__":
    pass
