import logging
import mysql.connector
from app.adapters.db_adapters.idatabase_adapter import IDatabaseAdapter


class MysqlAdapter(IDatabaseAdapter):
    def __init__(self, db_config):
        self.logger = logging.getLogger(__name__)
        self._db_config = db_config
        self._conn = self._connect()

    def _connect(self):
        try:
            conn = mysql.connector.connect(**self._db_config)
            logging.info(f"🟢 MySQL DB 連線成功")
            return conn
        except mysql.connector.Error as e:
            logging.error(f"🔴 MySQL DB 連線錯誤: {e}")
        except Exception as e:
            logging.error(f"🔴 MySQL DB 連線發生非預期錯誤: {e}")

    def insert(self, sql, params=None):
        """
        插入資料
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql, params)
            self._conn.commit()
            logging.info(f"🟢 新增 MySQL 資料成功")
        except mysql.connector.Error as e:
            logging.error(f"🔴 新增 MySQL 資料失敗: {e}")
            self._conn.rollback()
        finally:
            cursor.close()

    def fetch_all(self, sql, params=None):
        """
        讀取多筆資料
        """
        cursor = self._conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, params)
            read_data = cursor.fetchall()
            logging.info(f"🟢 查詢 MySQL 資料成功")
            return read_data
        except mysql.connector.Error as e:
            logging.error(f"🔴 查詢 MySQL 資料失敗: {e}")
        finally:
            cursor.close()

    def close(self):
        """
        關閉資料庫連線
        """
        try:
            self._conn.close()
            logging.info(f"🟢 MySQL DB 連線已關閉")
        except Exception as e:
            logging.error(f"🔴 MySQL DB 關閉連線非預期錯誤: {e}")


if __name__ == "__main__":
    pass
