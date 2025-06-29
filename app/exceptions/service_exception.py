from typing import Any, Optional
from app.exceptions.base_app_exception import BaseAppException
from app.exceptions.app_error_codes import AppErrorCodes


class ServiceBaseError(BaseAppException):
    """
    服務層通用錯誤。
    """

    def __init__(self, message: Optional[str] = None, details: Optional[Any] = None,
                 status_code=500, error_code: AppErrorCodes = AppErrorCodes.SERVICE_ERROR):
        super().__init__(
            error_code=error_code,
            status_code=status_code,
            message=message,
            details=details
        )


class BusinessLogicError(ServiceBaseError):
    """
    商業邏輯錯誤
    """

    def __init__(self, message: Optional[str] = None, details: Optional[Any] = None,
                 error_code: AppErrorCodes = AppErrorCodes.BUSINESS_LOGIC_ERROR):
        super().__init__(
            error_code=error_code,
            status_code=400,
            message=message,
            details=details
        )
