from unittest.mock import MagicMock, patch
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json
from auth_service.models import User
from shipping_service.models import Country, Address, UserAddress
from product_service.models import Product
from order_service.constants import OrderMethod, OrderStatus

# Global variables
CONTENT_TYPE = "application/json"

# Initialize the APIClient app
client = APIClient()

class RazorPayOrderAPITestCase(APITestCase):
    """ Test module to create a razorpay order using RazorPayOrderAPIView API """

    def get_url(self):
        url = reverse("razorpay_orders")
        return url

    def setUp(self):
        self.user = User.objects.create_user(email = "testuser@example.com", password = "abcdef")
        client.force_authenticate(user = self.user)

    @patch("order_service.views.razorpay_api_client")
    def test_create_razorpay_order_success(self, mock_razorpay_api_client):
        mock_create_order = MagicMock()
        mock_razorpay_api_client.create_order = mock_create_order
        mock_create_order.return_value = { "id" : "order_xyz", "amount" : 100, "currency" : "INR", "status" : "created" }

        url = self.get_url()
        data = json.dumps({ "amount" : 1 })
        response = client.post(url, data, content_type=CONTENT_TYPE)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual({ "id" : "order_xyz", "amount" : 100, "currency" : "INR", "status" : "created" }, response.data)

    @patch("order_service.views.razorpay_api_client")
    def test_create_razorpay_order_failure(self, mock_razorpay_api_client):
        mock_create_order = MagicMock()
        mock_razorpay_api_client.create_order = mock_create_order

        url = self.get_url()
        data = json.dumps({})
        response = client.post(url, data, content_type = CONTENT_TYPE)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This field is required.", str(response.data["amount"][0]))

class OrderAPITestCase(APITestCase):
    """ Test module to create an order using OrderAPIView API """
    def get_url(self):
        url = reverse("orders")
        return url

    def setUp(self):
        self.user = User.objects.create_user(email = "testuser@example.com", password = "abcdef")
        client.force_authenticate(user = self.user)
        self.country = Country.objects.create(name = "India")
        self.address = Address.objects.create(
            line1 = "abc", line2 = "def", city = "pqr", state = "xyz", country = self.country, pin_code = "123244"
        )
        self.user_address = UserAddress.objects.create(
            name = "test_user", user = self.user, address = self.address, alternate_phone = "1234567890", type = "Home",
            is_default = False
        )
        self.product = Product.objects.create(name="Canon 80D", description="good product", price=50000, stock_count=10)

    @patch("order_service.views.razorpay_api_client")
    def test_create_upi_order_success(self, mock_razorpay_api_client):
        mock_verify_payment_signature = MagicMock()
        mock_razorpay_api_client.utility.verify_payment_signature = mock_verify_payment_signature
        mock_verify_payment_signature.return_value = { "razorpay_signature": "verified_signature" }

        url = self.get_url()
        data = json.dumps({
            "razorpay_order_id": "order_xyz",
            "razorpay_payment_id": "payment_xyz",
            "razorpay_signature": "verified_signature",
            "user_address": self.user_address.pk,
            "amount": 100,
            "method": OrderMethod.UPI,
            "order_items": [{
                "product": self.product.pk,
                "quantity": 2
            }]
        })
        response = client.post(url, data, content_type=CONTENT_TYPE)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(response.data["is_paid"])
        self.assertEqual(OrderStatus.CONFIRMED, response.data["status"])
        self.assertEqual(str(self.user), response.data["user"])

    @patch("order_service.views.razorpay_api_client")
    def test_create_upi_order_failure(self, mock_razorpay_api_client):
        mock_verify_payment_signature = MagicMock()
        mock_razorpay_api_client.utility.verify_payment_signature = mock_verify_payment_signature
        mock_verify_payment_signature.return_value = { "razorpay_signature": "verified_signature" }

        url = self.get_url()
        data = json.dumps({
            "razorpay_order_id": "order_xyz",
            "razorpay_payment_id": "payment_xyz",
            "razorpay_signature": "verified_signature",
            "amount": 100,
            "method": OrderMethod.UPI,
            "order_items": [{
                "product": self.product.pk,
                "quantity": 2
            }]
        })
        response = client.post(url, data, content_type = CONTENT_TYPE)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This field is required.", str(response.data["user_address"][0]))

    def test_create_cod_order_success(self):
        url = self.get_url()
        data = json.dumps({
            "razorpay_order_id": None,
            "razorpay_payment_id": None,
            "razorpay_signature": None,
            "user_address": self.user_address.pk,
            "amount": 100,
            "method": OrderMethod.COD,
            "order_items": [{
                "product": self.product.pk,
                "quantity": 2
            }]
        })
        response = client.post(url, data, content_type=CONTENT_TYPE)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertFalse(response.data["is_paid"])
        self.assertEqual(OrderStatus.CONFIRMED, response.data["status"])
        self.assertEqual(str(self.user), response.data["user"])

    def test_create_cod_order_failure(self):
        url = self.get_url()
        data = json.dumps({
            "razorpay_order_id": None,
            "razorpay_payment_id": None,
            "razorpay_signature": None,
            "amount": 100,
            "method": OrderMethod.COD,
            "order_items": [{
                "product": self.product.pk,
                "quantity": 2
            }]
        })
        response = client.post(url, data, content_type=CONTENT_TYPE)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This field is required.", str(response.data["user_address"][0]))