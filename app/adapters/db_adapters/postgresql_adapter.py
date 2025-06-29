import logging
import psycopg2
from app.adapters.db_adapters.idatabase_adapter import IDatabaseAdapter


class PostgresqlAdapter(IDatabaseAdapter):
    def __init__(self, db_config):
        self.logger = logging.getLogger(__name__)
        self._db_config = db_config
        self._conn = self._connect()

    def _connect(self):
        try:
            conn = psycopg2.connect(**self._db_config)
            logging.info(f"🟢 PostgreSQL DB 連線成功")
            return conn
        except psycopg2.Error as e:
            raise psycopg2.Error(f"🔴[DEBUG]: PostgreSQL DB 連線錯誤: {e}")
        except Exception as e:
            raise psycopg2.Error(f"🔴[DEBUG]: PostgreSQL DB 連線發生非預期錯誤: {e}")

    def insert(self, sql, params=None):
        """
        插入資料
        """
        cursor = self._conn.cursor()
        try:
            cursor.execute(sql, params)
            self._conn.commit()
        except psycopg2.Error as e:
            self._conn.rollback()
            raise psycopg2.Error(f"🔴[DEBUG]: 新增 PostgreSQL 資料失敗: {e}")
        except Exception as e:
            self._conn.rollback()
            raise psycopg2.Error(f"🔴[DEBUG]: 新增 PostgreSQL 資料發生非預期錯誤: {e}")
        finally:
            cursor.close()

    def fetch_all(self, sql, params=None):
        """
        讀取資料
        """
        cursor = self._conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, params)
            read_data = cursor.fetchall()
            return read_data
        except psycopg2.Error as e:
            raise psycopg2.Error(f"🔴[DEBUG]: 查詢 PostgreSQL 資料失敗: {e}")
        except Exception as e:
            raise psycopg2.Error(f"🔴[DEBUG]: 查詢 PostgreSQL 資料發生非預期錯誤: {e}")
        finally:
            cursor.close()

    def close(self):
        """
        關閉資料庫連線
        """
        try:
            self._conn.close()
            logging.info(f"🟢 PostgreSQL DB 連線已關閉")
        except psycopg2.Error as e:
            raise psycopg2.Error(f"🔴[DEBUG]: PostgreSQL DB 關閉連線錯誤: {e}")
        except Exception as e:
            raise psycopg2.Error(f"🔴[DEBUG]: PostgreSQL DB 關閉連線非預期錯誤: {e}")


if __name__ == "__main__":
    pass
