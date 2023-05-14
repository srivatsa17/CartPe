from django.test import TestCase
from product_service.models import Category

class ProductModelTest(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="Men", description="Clothing", parent = None)

    def test_str_is_equal_to_title(self):
        product = Category.objects.get(name = "Men")
        expectedResponse = product.name
        receivedResponse = str(product)

        self.assertEqual(receivedResponse, expectedResponse)