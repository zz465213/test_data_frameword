from typing import Any, Optional
from app.exceptions.base_app_exception import BaseAppException
from app.exceptions.app_error_codes import AppErrorCodes


class CustomException(BaseAppException):
    """
    表示使用者輸入資料無效的通用異常，對應 HTTP 400。
    """

    def __init__(self, message: Optional[str] = None, details: Optional[Any] = None,
                 status_code=400, error_code: AppErrorCodes = AppErrorCodes.BAD_REQUEST_ERROR):
        super().__init__(
            error_code=error_code,
            status_code=status_code,
            message=message,
            details=details
        )


class InvalidPhoneFormatException(CustomException):
    """
    表示手機號碼格式不正確的異常。
    """

    def __init__(self, phone_no: str = None):
        super().__init__(
            error_code=AppErrorCodes.INVALID_PHONE_FORMAT,
            status_code=400,
            message=f"不合理的手機格式: {phone_no}. 必須為 09 開頭且為 10 碼。",
            details={"invalid_value": phone_no}
        )


class ValueBelowMinError(CustomException):
    """
    小於min的數值異常。
    """

    def __init__(self, current_no: int, min_no: int):
        super().__init__(
            error_code=AppErrorCodes.VALUE_BELOW_MIN_ERROR,
            status_code=400,
            message=f"當前數值為 {current_no}, 最小值 {min_no}.",
            details={"field": current_no, "min_length": min_no}
        )


class ValueAboveMaxError(CustomException):
    """
    大於max的數值異常。
    """

    def __init__(self, current_no: int, max_no: int):
        super().__init__(
            error_code=AppErrorCodes.VALUE_ABOVE_MAX_ERROR,
            status_code=400,
            message=f"當前數值為{current_no}, 大於最大值 {max_no}.",
            details={"field": current_no, "max_length": max_no}
        )
