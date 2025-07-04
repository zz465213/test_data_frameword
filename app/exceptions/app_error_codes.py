from enum import Enum


class AppErrorCodes(Enum):
    """
    應用程式內部的自定義錯誤碼枚舉。
    為每個 HTTP 狀態碼和更細粒度的應用程式錯誤定義唯一識別碼。
    """
    # 通用錯誤碼範圍 (500xx)
    UNEXPECTED_ERROR = 50000
    GENERIC_INTERNAL_SERVER_ERROR = 50001
    NOT_IMPLEMENTED_ERROR = 501
    BAD_GATEWAY_ERROR = 502
    SERVICE_UNAVAILABLE_ERROR = 503
    GATEWAY_TIMEOUT_ERROR = 504
    HTTP_VERSION_NOT_SUPPORTED_ERROR = 505
    VARIANT_ALSO_NEGOTIATES_ERROR = 506
    INSUFFICIENT_STORAGE_ERROR = 507
    LOOP_DETECTED_ERROR = 508
    NOT_EXTENDED_ERROR = 510
    NETWORK_AUTHENTICATION_REQUIRED_ERROR = 511

    # 客戶端錯誤碼範圍 (400xx)
    BAD_REQUEST_ERROR = 400
    UNAUTHORIZED_ERROR = 401
    PAYMENT_REQUIRED_ERROR = 402
    FORBIDDEN_ERROR = 403
    NOT_FOUND_ERROR = 404
    METHOD_NOT_ALLOWED_ERROR = 405
    NOT_ACCEPTABLE_ERROR = 406
    PROXY_AUTHENTICATION_REQUIRED_ERROR = 407
    REQUEST_TIMEOUT_ERROR = 408
    CONFLICT_ERROR = 409
    GONE_ERROR = 410
    LENGTH_REQUIRED_ERROR = 411
    PRECONDITION_FAILED_ERROR = 412
    REQUEST_ENTITY_TOO_LARGE_ERROR = 413
    REQUEST_URI_TOO_LONG_ERROR = 414
    UNSUPPORTED_MEDIA_TYPE_ERROR = 415
    REQUESTED_RANGE_NOT_SATISFIABLE_ERROR = 416
    EXPECTATION_FAILED_ERROR = 417
    IM_A_TEAPOT_ERROR = 418
    MISDIRECTED_REQUEST_ERROR = 421
    UNPROCESSABLE_ENTITY_ERROR = 422
    LOCKED_ERROR = 423
    FAILED_DEPENDENCY_ERROR = 424
    TOO_EARLY_ERROR = 425
    UPGRADE_REQUIRED_ERROR = 426
    PRECONDITION_REQUIRED_ERROR = 428
    TOO_MANY_REQUESTS_ERROR = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE_ERROR = 431
    UNAVAILABLE_FOR_LEGAL_REASONS_ERROR = 451

    # 自定義的格式錯誤碼
    VALUE_BELOW_MIN_ERROR = "M001"
    VALUE_ABOVE_MAX_ERROR = "M002"
    INVALID_PHONE_FORMAT = "M003"

    # 自定義的資料庫錯誤碼
    DATABASE_EXCEPTION = "D001"
    DATABASE_CONNECT_ERROR = "D002"
    DATABASE_INSERT_ERROR = "D003"
    DATABASE_FETCH_FAIL_ERROR = "D004"
    DATA_NOT_FOUND_ERROR = "D005"
    DUPLICATE_ENTRY_ERROR = "D006"  # 嘗試插入重複資料時拋出(唯一值會出現)

    # 自定義服務錯誤碼
    SERVICE_ERROR = "S001"
    INVALID_INPUT_ERROR = "S002"
    BUSINESS_LOGIC_ERROR = "S003"
    UNAUTHORIZED_ACCESS_ERROR = "S004"
    RESOURCE_CONFLICT_ERROR = "S005"

    def __str__(self):
        return f"{self.name} ({self.value})"

    def __repr__(self):
        return f"<AppErrorCodes.{self.name}: {self.value}>"
