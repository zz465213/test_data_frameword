import logging
import mysql.connector
from app.adapters.db_adapters.idatabase_adapter import IDatabaseAdapter


class MysqlAdapter(IDatabaseAdapter):
    def __init__(self, host, user, password, database):
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db_config = self._db_config()
        self.conn = self._connect()

    def _connect(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            logging.info(f"🟢 MySQL DB 連線成功")
            return conn
        except mysql.connector.Error as e:
            logging.error(f"🔴 MySQL DB 連線錯誤: {e}")
        except Exception as e:
            logging.error(f"🔴 MySQL DB 連線發生非預期錯誤: {e}")

    def _db_config(self):
        db_config = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "database": self.database
        }
        return db_config

    def insert(self, sql):
        """
        插入資料
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            logging.info(f"🟢 新增資料成功")
        except mysql.connector.Error as e:
            logging.error(f"🔴 新增資料失敗: {e}")
            self.conn.rollback()
            self.close()
        finally:
            cursor.close()

    def read(self, sql):
        """
        讀取資料
        """
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            read_data = cursor.fetchall()
            logging.info(f"🟢 查詢資料成功")
            return read_data
        except mysql.connector.Error as e:
            logging.error(f"🔴 查詢資料失敗: {e}")
            self.close()
        finally:
            cursor.close()

    def close(self):
        """
        關閉資料庫連線
        """
        try:
            self.conn.close()
            logging.info(f"🟢 MySQL DB 連線已關閉")
        except Exception as e:
            logging.error(f"🔴 MySQL DB 關閉連線非預期錯誤: {e}")


if __name__ == "__main__":
    pass