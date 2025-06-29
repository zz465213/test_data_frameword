from app.exceptions.base_app_exception import BaseAppException
from app.exceptions.app_error_codes import AppErrorCodes


class DatabaseException(BaseAppException):
    """資料庫操作的基礎例外類別"""

    def __init__(self, message: str = "🔴[DEBUG]: 資料庫發生非預期錯誤訊息",
                 status_code: int = 500,
                 error_code: AppErrorCodes = AppErrorCodes.DATABASE_EXCEPTION):
        super().__init__(message=message, status_code=status_code, error_code=error_code)


class DatabaseInsertException(DatabaseException):
    """資料庫Insert操作相關的例外"""

    def __init__(self, message: str = "🔴[DEBUG]: 資料庫發生「插入」錯誤訊息",
                 status_code: int = 500,
                 error_code: AppErrorCodes = AppErrorCodes.DATABASE_INSERT_ERROR):
        super().__init__(message=message, status_code=status_code, error_code=error_code)


class DatabaseFetchFailException(DatabaseException):
    """資料庫Fetch All操作相關的例外"""

    def __init__(self, message: str = "🔴[DEBUG]: 資料庫發生「搜尋」錯誤訊息",
                 status_code: int = 500,
                 error_code: AppErrorCodes = AppErrorCodes.DATABASE_FETCH_FAIL_ERROR):
        super().__init__(message=message, status_code=status_code, error_code=error_code)


class DatabaseConnectException(DatabaseException):
    """資料庫連線相關的例外"""

    def __init__(self, message: str = "🔴[DEBUG]: 資料庫發生「連線」錯誤訊息",
                 status_code: int = 500,
                 error_code: AppErrorCodes = AppErrorCodes.DATABASE_CONNECT_ERROR):
        super().__init__(message=message, status_code=status_code, error_code=error_code)


class DataNotFoundError(DatabaseException):
    """查詢不到資料的錯誤"""

    def __init__(self, message: str = "🔴[DEBUG]: 查無資料",
                 status_code: int = 400,
                 error_code: AppErrorCodes = AppErrorCodes.DATA_NOT_FOUND_ERROR):
        super().__init__(message=message, status_code=status_code, error_code=error_code)


class DuplicateEntryError(DatabaseException):
    """嘗試創建或修改資源時，唯一約束的狀態衝突。"""

    def __init__(self, message: str = "🔴[DEBUG]: 唯一約束的狀態衝突",
                 status_code: int = 409,
                 error_code: AppErrorCodes = AppErrorCodes.DUPLICATE_ENTRY_ERROR):
        super().__init__(message=message, status_code=status_code, error_code=error_code)
