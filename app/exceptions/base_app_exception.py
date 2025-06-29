from app.exceptions.app_error_codes import AppErrorCodes


class BaseAppException(Exception):
    """
    自定義異常的基類。

    - message (str): 錯誤的描述性訊息，通常會顯示給使用者或用於日誌。
    - error_code (int): 一個內部定義的數字錯誤碼，用於程式內部識別錯誤類型。
    - status_code (int, optional): 建議對應的 HTTP 狀態碼，如果未指定，預設為 500。
    - details (dict, optional): 任何額外的結構化錯誤細節，例如驗證錯誤的欄位資訊。
    - original_error (Exception, optional): 捕獲到的原始底層異常，方便日誌記錄和除錯。
    """

    def __init__(self,
                 message: str = "🔴DEBUG: 發生非預期錯誤",
                 error_code: AppErrorCodes = AppErrorCodes.UNEXPECTED_ERROR,
                 status_code: int = 500,
                 details: dict = None,
                 original_error: Exception = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details if details is not None else {}
        self.original_error = original_error

    def to_dict(self) -> dict:
        error_dict = {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "error_code": self.error_code.value,
            "status_code": self.status_code
        }
        if self.details:
            error_dict["details"] = self.details
        return error_dict


# == Client Error Exceptions (4xx 系列) ==
class BadRequestError(BaseAppException):
    """400 Bad Request: 錯誤的請求語法或不支援的方法。"""

    def __init__(self, message: str = "Bad request syntax or unsupported method.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.BAD_REQUEST_ERROR,
            status_code=400,
            details=details
        )


class UnauthorizedError(BaseAppException):
    """401 Unauthorized: 沒有權限 -- 需要認證。"""

    def __init__(self, message: str = "No permission -- see authorization schemes.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.UNAUTHORIZED_ERROR,
            status_code=401,
            details=details
        )


class PaymentRequiredError(BaseAppException):
    """402 Payment Required: 沒有支付 -- 需要付款。"""

    def __init__(self, message: str = "No payment -- see charging schemes.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.PAYMENT_REQUIRED_ERROR,
            status_code=402,
            details=details
        )


class ForbiddenError(BaseAppException):
    """403 Forbidden: 請求被禁止 -- 認證也無效。"""

    def __init__(self, message: str = "Request forbidden -- authorization will not help.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.FORBIDDEN_ERROR,
            status_code=403,
            details=details
        )


class NotFoundError(BaseAppException):
    """404 Not Found: 沒有匹配給定 URI 的資源。"""

    def __init__(self, message: str = "Nothing matches the given URI.", resource_id: str = None, details: dict = None):
        if resource_id:
            message = f"Resource with ID '{resource_id}' not found."
        super().__init__(
            message,
            error_code=AppErrorCodes.NOT_FOUND_ERROR,
            status_code=404,
            details=details
        )
        self.resource_id = resource_id  # 新增屬性，便於追溯


class MethodNotAllowedError(BaseAppException):
    """405 Method Not Allowed: 指定的方法對於此資源無效。"""

    def __init__(self, message: str = "Specified method is invalid for this resource.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.METHOD_NOT_ALLOWED_ERROR,
            status_code=405,
            details=details
        )


class NotAcceptableError(BaseAppException):
    """406 Not Acceptable: URI 無法以偏好格式提供。"""

    def __init__(self, message: str = "URI not available in preferred format.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.NOT_ACCEPTABLE_ERROR,
            status_code=406,
            details=details
        )


class ProxyAuthenticationRequiredError(BaseAppException):
    """407 Proxy Authentication Required: 在繼續之前，您必須使用此代理進行認證。"""

    def __init__(self, message: str = "You must authenticate with this proxy before proceeding.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.PROXY_AUTHENTICATION_REQUIRED_ERROR,
            status_code=407,
            details=details
        )


class RequestTimeoutError(BaseAppException):
    """408 Request Timeout: 請求超時；請稍後重試。"""

    def __init__(self, message: str = "Request timed out; try again later.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.REQUEST_TIMEOUT_ERROR,
            status_code=408,
            details=details
        )


class ConflictError(BaseAppException):
    """409 Conflict: 請求衝突。"""

    def __init__(self, message: str = "Request conflict.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.CONFLICT_ERROR,
            status_code=409,
            details=details
        )


class GoneError(BaseAppException):
    """410 Gone: URI 不再存在且已被永久移除。"""

    def __init__(self, message: str = "URI no longer exists and has been permanently removed.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.GONE_ERROR,
            status_code=410,
            details=details
        )


class LengthRequiredError(BaseAppException):
    """411 Length Required: 客戶端必須指定 Content-Length。"""

    def __init__(self, message: str = "Client must specify Content-Length.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.LENGTH_REQUIRED_ERROR,
            status_code=411,
            details=details
        )


class PreconditionFailedError(BaseAppException):
    """412 Precondition Failed: 標頭中的前置條件為假。"""

    def __init__(self, message: str = "Precondition in headers is false.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.PRECONDITION_FAILED_ERROR,
            status_code=412,
            details=details
        )


class RequestEntityTooLargeError(BaseAppException):
    """413 Request Entity Too Large: 實體過大。"""

    def __init__(self, message: str = "Entity is too large.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.REQUEST_ENTITY_TOO_LARGE_ERROR,
            status_code=413,
            details=details
        )


class RequestURITooLongError(BaseAppException):
    """414 Request-URI Too Long: URI 過長。"""

    def __init__(self, message: str = "URI is too long.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.REQUEST_URI_TOO_LONG_ERROR,
            status_code=414,
            details=details
        )


class UnsupportedMediaTypeError(BaseAppException):
    """415 Unsupported Media Type: 實體內容格式不受支援。"""

    def __init__(self, message: str = "Entity body in unsupported format.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.UNSUPPORTED_MEDIA_TYPE_ERROR,
            status_code=415,
            details=details
        )


class RequestedRangeNotSatisfiableError(BaseAppException):
    """416 Requested Range Not Satisfiable: 無法滿足請求範圍。"""

    def __init__(self, message: str = "Cannot satisfy request range.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.REQUESTED_RANGE_NOT_SATISFIABLE_ERROR,
            status_code=416,
            details=details
        )


class ExpectationFailedError(BaseAppException):
    """417 Expectation Failed: 預期條件無法滿足。"""

    def __init__(self, message: str = "Expect condition could not be satisfied.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.EXPECTATION_FAILED_ERROR,
            status_code=417,
            details=details
        )


class ImATeapotError(BaseAppException):
    """418 I'm a Teapot: 伺服器拒絕泡咖啡，因為它是茶壺。 (HTCPCP/1.0 玩笑錯誤碼)"""

    def __init__(self, message: str = "Server refuses to brew coffee because it is a teapot.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.IM_A_TEAPOT_ERROR,
            status_code=418,
            details=details
        )


class MisdirectedRequestError(BaseAppException):
    """421 Misdirected Request: 伺服器無法產生響應。"""

    def __init__(self, message: str = "Server is not able to produce a response.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.MISDIRECTED_REQUEST_ERROR,
            status_code=421,
            details=details
        )


class UnprocessableEntityError(BaseAppException):
    """422 Unprocessable Entity: 請求格式正確，但語義錯誤。"""

    def __init__(self,
                 message: str = "The request was well-formed but was unable to be followed due to semantic errors.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.UNPROCESSABLE_ENTITY_ERROR,
            status_code=422,
            details=details
        )


class LockedError(BaseAppException):
    """423 Locked: 資源被鎖定。"""

    def __init__(self, message: str = "The resource is locked.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.LOCKED_ERROR,
            status_code=423,
            details=details
        )


class FailedDependencyError(BaseAppException):
    """424 Failed Dependency: 請求失敗，因為依賴的請求也失敗了。"""

    def __init__(self, message: str = "The request failed because it depended on another request that failed.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.FAILED_DEPENDENCY_ERROR,
            status_code=424,
            details=details
        )


class TooEarlyError(BaseAppException):
    """425 Too Early: 伺服器不願處理請求，因為它可能在後續重複。"""

    def __init__(self, message: str = "The server is unwilling to process the request because it might be replayed.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.TOO_EARLY_ERROR,
            status_code=425,
            details=details
        )


class UpgradeRequiredError(BaseAppException):
    """426 Upgrade Required: 客戶端應切換到不同協議。"""

    def __init__(self, message: str = "The client should switch to a different protocol.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.UPGRADE_REQUIRED_ERROR,
            status_code=426,
            details=details
        )


class PreconditionRequiredError(BaseAppException):
    """428 Precondition Required: 源伺服器要求請求是條件性的。"""

    def __init__(self, message: str = "The origin server requires the request to be conditional.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.PRECONDITION_REQUIRED_ERROR,
            status_code=428,
            details=details
        )


class TooManyRequestsError(BaseAppException):
    """429 Too Many Requests: 用戶在給定時間內發送了太多請求（“速率限制”）。"""

    def __init__(self,
                 message: str = "The user has sent too many requests in a given amount of time ('rate limiting').",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.TOO_MANY_REQUESTS_ERROR,
            status_code=429,
            details=details
        )


class RequestHeaderFieldsTooLargeError(BaseAppException):
    """431 Request Header Fields Too Large: 伺服器不願處理請求，因為其標頭欄位過大。"""

    def __init__(self,
                 message: str = "The server is unwilling to process the request because its header fields are too large.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.REQUEST_HEADER_FIELDS_TOO_LARGE_ERROR,
            status_code=431,
            details=details
        )


class UnavailableForLegalReasonsError(BaseAppException):
    """451 Unavailable For Legal Reasons: 伺服器因法律要求拒絕訪問資源。"""

    def __init__(self,
                 message: str = "The server is denying access to the resource as a consequence of a legal demand.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.UNAVAILABLE_FOR_LEGAL_REASONS_ERROR,
            status_code=451,
            details=details
        )


# == Server Error Exceptions (5xx 系列) ==s
class InternalServerError(BaseAppException):
    """500 Internal Server Error: 伺服器自身出錯。"""

    def __init__(self, message: str = "An unexpected internal server error occurred.", details: dict = None,
                 original_error: Exception = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.GENERIC_INTERNAL_SERVER_ERROR,
            status_code=500,
            details=details,
            original_error=original_error
        )


class NotImplementedError(BaseAppException):
    """501 Not Implemented: 伺服器不支援此操作。"""

    def __init__(self, message: str = "Server does not support this operation.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.NOT_IMPLEMENTED_ERROR,
            status_code=501,
            details=details
        )


class BadGatewayError(BaseAppException):
    """502 Bad Gateway: 從另一個伺服器/代理收到無效響應。"""

    def __init__(self, message: str = "Invalid responses from another server/proxy.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.BAD_GATEWAY_ERROR,
            status_code=502,
            details=details
        )


class ServiceUnavailableError(BaseAppException):
    """503 Service Unavailable: 伺服器因負載過高無法處理請求。"""

    def __init__(self, message: str = "The server cannot process the request due to a high load.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.SERVICE_UNAVAILABLE_ERROR,
            status_code=503,
            details=details
        )


class GatewayTimeoutError(BaseAppException):
    """504 Gateway Timeout: 網關伺服器未收到及時響應。"""

    def __init__(self, message: str = "The gateway server did not receive a timely response.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.GATEWAY_TIMEOUT_ERROR,
            status_code=504,
            details=details
        )


class HTTPVersionNotSupportedError(BaseAppException):
    """505 HTTP Version Not Supported: 無法滿足請求。"""

    def __init__(self, message: str = "Cannot fulfill request.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.HTTP_VERSION_NOT_SUPPORTED_ERROR,
            status_code=505,
            details=details
        )


class VariantAlsoNegotiatesError(BaseAppException):
    """506 Variant Also Negotiates: 伺服器存在內部配置錯誤。"""

    def __init__(self, message: str = "The server has an internal configuration error.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.VARIANT_ALSO_NEGOTIATES_ERROR,
            status_code=506,
            details=details
        )


class InsufficientStorageError(BaseAppException):
    """507 Insufficient Storage: 伺服器無法執行請求，因為沒有足夠的空間。"""

    def __init__(self,
                 message: str = "The server is unable to store the representation needed to complete the request.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.INSUFFICIENT_STORAGE_ERROR,
            status_code=507,
            details=details
        )


class LoopDetectedError(BaseAppException):
    """508 Loop Detected: 伺服器在處理請求時檢測到無限循環。"""

    def __init__(self, message: str = "The server detected an infinite loop while processing the request.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.LOOP_DETECTED_ERROR,
            status_code=508,
            details=details
        )


class NotExtendedError(BaseAppException):
    """510 Not Extended: 請求需要擴展才能完成。"""

    def __init__(self, message: str = "Further extensions to the request are needed for it to be fulfilled.",
                 details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.NOT_EXTENDED_ERROR,
            status_code=510,
            details=details
        )


class NetworkAuthenticationRequiredError(BaseAppException):
    """511 Network Authentication Required: 客戶端需要認證才能獲得網路訪問權限。"""

    def __init__(self, message: str = "The client needs to authenticate to gain network access.", details: dict = None):
        super().__init__(
            message,
            error_code=AppErrorCodes.NETWORK_AUTHENTICATION_REQUIRED_ERROR,
            status_code=511,
            details=details
        )
