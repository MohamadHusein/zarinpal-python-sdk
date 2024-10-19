import unittest
from zarinpal.client import ZarinpalClient
from unittest.mock import patch

class TestZarinpalClient(unittest.TestCase):

    def setUp(self):
        # تنظیمات اولیه برای هر تست
        self.client = ZarinpalClient(merchant_id="test_merchant_id", sandbox=True)

    @patch('requests.post')
    def test_request_payment(self, mock_post):
        # شبیه‌سازی پاسخ موفق از API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100, 'Authority': 'TestAuthority'}

        response = self.client.request_payment(1000, "Test payment", "http://example.com/callback")
        self.assertEqual(response['Status'], 100)
        self.assertEqual(response['Authority'], 'TestAuthority')

    @patch('requests.post')
    def test_verify_payment(self, mock_post):
        # شبیه‌سازی پاسخ موفق برای تایید پرداخت
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100}

        response = self.client.verify_payment("TestAuthority", 1000)
        self.assertEqual(response['Status'], 100)

    @patch('requests.post')
    def test_inquiry_transaction(self, mock_post):
        # شبیه‌سازی پاسخ موفق برای استعلام تراکنش
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100}

        response = self.client.inquiry_transaction("TestAuthority")
        self.assertEqual(response['Status'], 100)

    @patch('requests.post')
    def test_get_unverified_transactions(self, mock_post):
        # شبیه‌سازی پاسخ برای دریافت تراکنش‌های تایید نشده
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100, 'Authorities': ['TestAuthority1', 'TestAuthority2']}

        response = self.client.get_unverified_transactions()
        self.assertEqual(response['Status'], 100)
        self.assertIn('TestAuthority1', response['Authorities'])

    @patch('requests.post')
    def test_reverse_transaction(self, mock_post):
        # شبیه‌سازی پاسخ موفق برای ریورس تراکنش
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100}

        response = self.client.reverse_transaction("TestAuthority")
        self.assertEqual(response['Status'], 100)

    @patch('requests.post')
    def test_refund_transaction(self, mock_post):
        # شبیه‌سازی پاسخ موفق برای استرداد وجه
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100}

        response = self.client.refund_transaction("TestAuthority", 1000)
        self.assertEqual(response['Status'], 100)

    @patch('requests.post')
    def test_get_transaction_details(self, mock_post):
        # شبیه‌سازی پاسخ موفق برای دریافت جزئیات تراکنش
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'Status': 100, 'Authority': 'TestAuthority'}

        response = self.client.get_transaction_details("TestAuthority")
        self.assertEqual(response['Status'], 100)
        self.assertEqual(response['Authority'], 'TestAuthority')


if __name__ == '__main__':
    unittest.main()
