import re

def get_status_message(status_code):
    """
    تبدیل کد وضعیت به پیام قابل فهم.
    این تابع بر اساس کد وضعیت (status code) ارائه‌شده، پیام مناسب را برمی‌گرداند.
    """
    status_messages = {
        -9: "خطای اعتبار سنجی: 1- مرچنت کد وارد نشده است، 2- آدرس بازگشت وارد نشده است، 3- توضیحات یا بیش از ۵۰۰ کاراکتر است یا وارد نشده است، 4- مبلغ پرداختی کمتر یا بیشتر از حد مجاز است.",
        -10: "ای پی یا مرچنت کد پذیرنده صحیح نیست.",
        -11: "مرچنت کد فعال نیست، لطفاً با پشتیبانی تماس بگیرید.",
        -12: "تلاش بیش از حد مجاز. لطفاً بعداً دوباره تلاش کنید.",
        -15: "درگاه پرداخت به حالت تعلیق درآمده است. لطفاً با پشتیبانی تماس بگیرید.",
        -16: "سطح تایید پذیرنده پایین‌تر از سطح نقره‌ای است.",
        -17: "محدودیت پذیرنده در سطح آبی.",
        100: "عملیات موفق.",
        -30: "پذیرنده اجازه دسترسی به سرویس تسویه اشتراکی شناور را ندارد.",
        -31: "حساب بانکی تسویه را به پنل اضافه کنید. مقادیر وارد شده برای تسهیم درست نیست.",
        -32: "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است.",
        -33: "درصدهای وارد شده صحیح نیست.",
        -34: "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است.",
        -35: "تعداد افراد دریافت کننده تسهیم بیش از حد مجاز است.",
        -36: "حداقل مبلغ جهت تسهیم باید ۱۰,۰۰۰ ریال باشد.",
        -37: "یک یا چند شماره شبای وارد شده برای تسهیم از سمت بانک غیر فعال است.",
        -38: "خطا٬ عدم تعریف صحیح شبا٬ لطفا دقایقی دیگر تلاش کنید.",
        -39: "خطایی رخ داده است. لطفاً با پشتیبانی تماس بگیرید.",
        -40: "پارامترهای اضافی نامعتبر هستند، expire_in معتبر نیست.",
        -41: "حداکثر مبلغ پرداختی ۱۰۰ میلیون تومان است.",
        -50: "مبلغ پرداخت شده با مبلغ ارسالی در متد وریفای متفاوت است.",
        -51: "پرداخت ناموفق.",
        -52: "خطای غیرمنتظره. لطفاً با پشتیبانی تماس بگیرید.",
        -53: "پرداخت متعلق به این مرچنت کد نیست.",
        -54: "اتوریتی نامعتبر است.",
        -55: "تراکنش مورد نظر یافت نشد.",
        -60: "امکان ریورس کردن تراکنش با بانک وجود ندارد.",
        -61: "تراکنش موفق نیست یا قبلاً ریورس شده است.",
        -62: "آی پی درگاه ست نشده است.",
        -63: "حداکثر زمان (۳۰ دقیقه) برای ریورس کردن این تراکنش منقضی شده است.",
        101: "تراکنش وریفای شده است."
    }
    return status_messages.get(status_code, "کد وضعیت ناشناخته")

def is_valid_email(email):
    """
    بررسی صحت فرمت ایمیل.
    این تابع بررسی می‌کند که آیا ایمیل ورودی با فرمت صحیح است یا خیر.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_mobile(mobile):
    """
    بررسی صحت فرمت شماره موبایل (ایران).
    این تابع بررسی می‌کند که شماره موبایل باید حتماً با '0' شروع شود و 11 رقم داشته باشد.
    """
    mobile_regex = r'^0\d{10}$'
    return re.match(mobile_regex, mobile) is not None


def get_zarinpal_base_url(sandbox=False):
    """
    بر اساس حالت انتخاب شده (آزمایشی یا واقعی)، آدرس URL مربوط به زرین‌پال را برمی‌گرداند.
    """
    if sandbox:
        return "https://sandbox.zarinpal.com/pg/rest/WebGate/"
    return "https://www.zarinpal.com/pg/rest/WebGate/"

def format_amount(amount):
    """
    فرمت دهی مبلغ به صورت صحیح (ریال).
    """
    return int(amount)

def is_valid_amount(amount):
    """
    بررسی صحت مقدار پرداخت.
    این تابع بررسی می‌کند که مقدار وارد شده معتبر است یا خیر (باید بیشتر از ۰ باشد).
    """
    return amount > 0
