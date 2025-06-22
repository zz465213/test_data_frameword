import logging
from app.adapters.db_adapters.postgresql_adapter import PostgresqlAdapter
from app.adapters.db_adapters.mysql_adapter import MysqlAdapter


class DBFactory:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def get_mysql(host, user, password, database) -> MysqlAdapter:
        """
        返回 My SQL 資料庫實體。
        """
        return MysqlAdapter(host, user, password, database)

    @staticmethod
    def get_postgresql(host, user, password, database) -> PostgresqlAdapter:
        """
        返回 PostgreSQL 資料庫實體。
        """
        return PostgresqlAdapter(host, user, password, database)


if __name__ == "__main__":
    pass
