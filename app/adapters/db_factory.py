import logging
from configs.common_paths import CONFIGS_FILE
from app.utils.file_tool import read_yaml
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
    db_factory = DBFactory()
    mysql = db_factory.get_mysql(
        host=read_yaml(CONFIGS_FILE)["mysql"]["host"],
        user=read_yaml(CONFIGS_FILE)["mysql"]["user"],
        password=read_yaml(CONFIGS_FILE)["mysql"]["password"],
        database=read_yaml(CONFIGS_FILE)["mysql"]["database"]
    )
    mysql.insert(
        sql="INSERT INTO member (username, email, phone, age) "
            "VALUES ('使用者名稱A', 'emailA@example.com', '0912345678', 30);")
    data = mysql.read(sql="SELECT * FROM member")
    mysql.close()
