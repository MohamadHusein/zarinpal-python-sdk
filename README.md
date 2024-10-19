# Zarinpal SDK for Python

این پکیج یک SDK برای تعامل با درگاه پرداخت زرین‌پال در زبان پایتون است. با استفاده از این SDK می‌توانید به راحتی عملیات‌های پرداخت، تایید پرداخت، استعلام تراکنش و موارد دیگر را در پروژه‌های پایتون و جنگو خود پیاده‌سازی کنید.

## نصب

### پیش‌نیازها

این پکیج برای کار با پایتون 3.6 به بالا توسعه داده شده است. برای استفاده از این پکیج ابتدا باید آن را نصب کنید.

### نصب با استفاده از pip

```
pip install zarinpal_sdk
```


نحوه استفاده
تنظیمات اولیه
برای استفاده از SDK، ابتدا باید merchant_id (مرچنت کد) خود را از پنل زرین‌پال دریافت کرده و آن را برای تعامل با درگاه پرداخت تنظیم کنید. همچنین، می‌توانید بین حالت آزمایشی (sandbox) و واقعی سوییچ کنید.
```
from zarinpal.client import ZarinpalClient

client = ZarinpalClient(merchant_id="your_merchant_id", sandbox=True)
```



درخواست پرداخت
برای شروع یک پرداخت جدید، می‌توانید از متد request_payment استفاده کنید:

```
response = client.request_payment(
    amount=11000,  # مبلغ به ریال
    description="خرید محصول تستی",  # توضیحات پرداخت
    callback_url="http://your-site.com/verify/",  # آدرس بازگشت
    mobile="09123456789",  # (اختیاری) شماره موبایل خریدار
    email="test@example.com"  # (اختیاری) ایمیل خریدار
)

if response['Status'] == 100:
    print(f"Redirect to: https://sandbox.zarinpal.com/pg/StartPay/{response['Authority']}")
else:
    print(f"Error: {response['Status']}")
```




تایید پرداخت
پس از بازگشت کاربر به سایت شما، می‌توانید از متد verify_payment برای تایید پرداخت استفاده کنید:

```
authority = request.GET.get('Authority')
response = client.verify_payment(authority=authority, amount=10000)

if response['Status'] == 100:
    print("پرداخت با موفقیت تایید شد.")
else:
    print("پرداخت ناموفق.")
```




استعلام تراکنش
برای بررسی وضعیت تراکنش‌ها می‌توانید از متد inquiry_transaction استفاده کنید:

```
response = client.inquiry_transaction(authority="YourAuthorityCode")
if response['Status'] == 100:
    print("تراکنش موفق.")
else:
    print(f"وضعیت تراکنش: {response['Status']}")
```





تراکنش‌های تایید نشده
برای دریافت لیستی از تراکنش‌های تایید نشده، از متد get_unverified_transactions استفاده کنید:

```
response = client.get_unverified_transactions()
if response['Status'] == 100:
    print("تراکنش‌های تایید نشده:", response['Authorities'])
else:
    print("خطا در دریافت تراکنش‌ها.")
```






ریورس تراکنش
برای لغو تراکنش، می‌توانید از متد reverse_transaction استفاده کنید:

```
response = client.reverse_transaction(authority="YourAuthorityCode")
if response['Status'] == 100:
    print("تراکنش با موفقیت لغو شد.")
else:
    print(f"خطا: {response['Status']}")
```





استرداد وجه
برای استرداد وجه یک تراکنش، می‌توانید از متد refund_transaction استفاده کنید:

```
response = client.refund_transaction(authority="YourAuthorityCode", amount=5000)
if response['Status'] == 100:
    print("وجه با موفقیت استرداد شد.")
else:
    print(f"خطا: {response['Status']}")
```






مدیریت خطاها
در SDK، خطاها و استثناهای مختلفی تعریف شده است که به شما کمک می‌کند تا بتوانید به سادگی مشکلات را مدیریت کنید. برای مثال، اگر در درخواست پرداخت خطایی رخ دهد، پیام خطا به صورت زیر نمایش داده می‌شود:


```
from zarinpal.exceptions import PaymentRequestError, NetworkError

try:
    response = client.request_payment(
        amount=11000,
        description="خرید محصول تستی",
        callback_url="http://your-site.com/verify/"
    )
except PaymentRequestError as e:
    print(f"خطا در درخواست پرداخت: {e}")
except NetworkError as e:
    print(f"خطای شبکه: {e}")
```






ابزارها (Utilities)
پکیج دارای توابع کمکی نیز می‌باشد که به شما در مدیریت بهتر کد کمک می‌کند. به عنوان مثال:

دریافت پیام خطای مرتبط با کد وضعیت:

```
from zarinpal.utils import get_status_message

status_code = -10
message = get_status_message(status_code)
print(message)  # خروجی: "ای پی یا مرچنت کد پذیرنده صحیح نیست."
```






بررسی فرمت ایمیل:

```
from zarinpal.utils import is_valid_email

email = "test@example.com"
if is_valid_email(email):
    print("ایمیل معتبر است.")
else:
    print("ایمیل نامعتبر است.")
```






بررسی فرمت شماره موبایل:

```
from zarinpal.utils import is_valid_mobile

mobile = "09123456789"
if is_valid_mobile(mobile):
    print("شماره موبایل معتبر است.")
else:
    print("شماره موبایل نامعتبر است.")
```




## توسعه و مشارکت

اگر می‌خواهید به توسعه‌ی این SDK کمک کنید یا باگ‌های موجود را گزارش دهید، می‌توانید به [لینک](https://github.com/MohamadHusein/zarinpal-python-sdk) مراجعه کنید و تغییرات پیشنهادی خود را از طریق Pull Request ارسال کنید.
























