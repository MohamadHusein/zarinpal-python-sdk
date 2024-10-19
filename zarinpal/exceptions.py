class ZarinpalException(Exception):
    """پایه‌ی تمامی استثناهای مربوط به زرین‌پال."""
    def __init__(self, message="An error occurred with Zarinpal API"):
        self.message = message
        super().__init__(self.message)

class PaymentRequestError(ZarinpalException):
    """خطا در هنگام درخواست پرداخت."""
    def __init__(self, status_code, response_message):
        self.status_code = status_code
        self.response_message = response_message
        self.message = f"Payment request failed with status code {self.status_code}: {self.response_message}"
        super().__init__(self.message)

class PaymentVerificationError(ZarinpalException):
    """خطا در هنگام تایید پرداخت."""
    def __init__(self, status_code, response_message):
        self.status_code = status_code
        self.response_message = response_message
        self.message = f"Payment verification failed with status code {self.status_code}: {self.response_message}"
        super().__init__(self.message)

class InquiryTransactionError(ZarinpalException):
    """خطا در هنگام استعلام تراکنش."""
    def __init__(self, status_code, response_message):
        self.status_code = status_code
        self.response_message = response_message
        self.message = f"Transaction inquiry failed with status code {self.status_code}: {self.response_message}"
        super().__init__(self.message)

class ReverseTransactionError(ZarinpalException):
    """خطا در هنگام ریورس تراکنش."""
    def __init__(self, status_code, response_message):
        self.status_code = status_code
        self.response_message = response_message
        self.message = f"Transaction reverse failed with status code {self.status_code}: {self.response_message}"
        super().__init__(self.message)

class RefundTransactionError(ZarinpalException):
    """خطا در هنگام استرداد وجه."""
    def __init__(self, status_code, response_message):
        self.status_code = status_code
        self.response_message = response_message
        self.message = f"Transaction refund failed with status code {self.status_code}: {self.response_message}"
        super().__init__(self.message)

class NetworkError(ZarinpalException):
    """خطاهای مربوط به شبکه، مانند عدم اتصال به سرور."""
    def __init__(self, message="Network error occurred while trying to communicate with Zarinpal"):
        self.message = message
        super().__init__(self.message)

class InvalidResponseError(ZarinpalException):
    """خطا در صورتی که پاسخ دریافتی از API نامعتبر باشد."""
    def __init__(self, message="Invalid response received from Zarinpal API"):
        self.message = message
        super().__init__(self.message)
