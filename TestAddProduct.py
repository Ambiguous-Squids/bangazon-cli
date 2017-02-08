import unittest
from customer import *
from order import *
from product import *

class TestAddProduct(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Customer(first_name="bob")
        self.new_product = Product('yoyo', 5)
        self.active_order = Order(self.bob)

    def test_OrderIsActive(self):
        self.assertTrue(self.active_order.active)

    def test_OrderBelongsToActiveCustomer(self):
        self.assertIs(self.bob, self.active_order.get_customer())

    def test_OrderIncludesProductAdded(self):
        self.active_order.add_product(self.new_product)
        self.assertIn(self.new_product, self.active_order.products)

    def test_PriceOfProductAddedIsAddedToOrderTotal(self):
        self.assertEqual(self.active_order.get_total(), self.active_order.add_product(self.new_product))

    def test_CanAddDuplicateProductsToOrder(self):
        pass

if __name__ == '__main__':
    unittest.main()