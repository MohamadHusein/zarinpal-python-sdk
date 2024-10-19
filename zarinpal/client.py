import requests

class ZarinpalClient:
    def __init__(self, merchant_id, sandbox=False):
        self.merchant_id = merchant_id
        self.sandbox = sandbox
        self.base_url = "https://sandbox.zarinpal.com/pg/rest/WebGate/" if sandbox else "https://www.zarinpal.com/pg/rest/WebGate/"

    # متد درخواست درگاه پرداخت
    def request_payment(self, amount, description, callback_url, mobile=None, email=None):
        url = self.base_url + "PaymentRequest.json"
        data = {
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Description": description,
            "CallbackURL": callback_url,
            "Mobile": mobile,
            "Email": email
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in payment request")

    # متد تایید پرداخت
    def verify_payment(self, authority, amount):
        url = self.base_url + "PaymentVerification.json"
        data = {
            "MerchantID": self.merchant_id,
            "Authority": authority,
            "Amount": amount
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in verifying payment")

    # متد استعلام تراکنش
    def inquiry_transaction(self, authority):
        url = self.base_url + "PaymentInquiry.json"
        data = {
            "MerchantID": self.merchant_id,
            "Authority": authority
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in inquiring transaction")

    # متد تراکنش‌های تایید نشده
    def get_unverified_transactions(self):
        url = self.base_url + "UnverifiedTransactions.json"
        data = {
            "MerchantID": self.merchant_id
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in getting unverified transactions")

    # متد ریورس تراکنش
    def reverse_transaction(self, authority):
        url = self.base_url + "ReverseTransaction.json"
        data = {
            "MerchantID": self.merchant_id,
            "Authority": authority
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in reversing transaction")

    # متد استرداد وجه
    def refund_transaction(self, authority, amount):
        url = self.base_url + "RefundTransaction.json"
        data = {
            "MerchantID": self.merchant_id,
            "Authority": authority,
            "Amount": amount
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in refunding transaction")

    # متد دریافت جزئیات تراکنش
    def get_transaction_details(self, authority):
        url = self.base_url + "GetTransaction.json"
        data = {
            "MerchantID": self.merchant_id,
            "Authority": authority
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in getting transaction details")
