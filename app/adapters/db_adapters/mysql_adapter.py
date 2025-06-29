import logging
import traceback
import mysql.connector
from app.exceptions.database_exception import *
from app.adapters.db_adapters.idatabase_adapter import IDatabaseAdapter


class MysqlAdapter(IDatabaseAdapter):
    def __init__(self, db_config):
        self._db_config = db_config
        self._conn = self._connect()

    def _connect(self):
        try:
            conn = mysql.connector.connect(**self._db_config)
            logging.info(f"🟢 MySQL DB 連線成功")
            return conn
        except mysql.connector.Error as e:
            raise DatabaseConnectException(f"🔴[DEBUG]: {__name__} 發生連線錯誤: {e}\n"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")
        except Exception as e:
            raise DatabaseConnectException(f"🔴[DEBUG]: {__name__} 發生非預期連線錯誤: {e}"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")

    def insert(self, sql, params=None):
        """
        插入資料
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql, params)
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            raise DatabaseInsertException(
                message=f"🔴[DEBUG]: {__name__} 發生「插入」錯誤訊息: {e}\n"
                        f"--- 打印錯誤追溯 ---\n"
                        f"{traceback.format_exc()}")
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
        except Exception as e:
            DatabaseFetchFailException(message=f"🔴[DEBUG]: {__name__} 發生「搜尋」錯誤訊息: {e}"
                                               f"--- 打印錯誤追溯 ---\n"
                                               f"{traceback.format_exc()}")
        finally:
            cursor.close()

    def close(self):
        """
        關閉資料庫連線
        """
        try:
            self._conn.close()
            logging.info(f"🟢 MySQL DB 連線已關閉")
        except mysql.connector.Error as e:
            raise DatabaseConnectException(f"🔴[DEBUG]: {__name__} 關閉連線錯誤: {e}"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")
        except Exception as e:
            raise DatabaseConnectException(f"🔴[DEBUG]: {__name__} 關閉連線非預期錯誤: {e}"
                                           f"--- 打印錯誤追溯 ---\n"
                                           f"{traceback.format_exc()}")


if __name__ == "__main__":
    pass
