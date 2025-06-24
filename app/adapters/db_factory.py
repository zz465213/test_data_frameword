import logging
from app.adapters.db_adapters.postgresql_adapter import PostgresqlAdapter
from app.adapters.db_adapters.mysql_adapter import MysqlAdapter
from app.utils.file_tool import read_yaml
from configs.common_paths import CONFIGS_FILE


class DBFactory:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._get_config = read_yaml(CONFIGS_FILE)

    def get_mysql(self) -> MysqlAdapter:
        """
        返回 My SQL 資料庫實體。
        """
        mysql_config = self._get_config["mysql"]
        return MysqlAdapter(mysql_config)

    def get_postgresql(self) -> PostgresqlAdapter:
        """
        返回 PostgreSQL 資料庫實體。
        """
        postgresql_config = self._get_config["postgresql"]
        return PostgresqlAdapter(postgresql_config)


if __name__ == "__main__":
    mysql = DBFactory().get_mysql()

