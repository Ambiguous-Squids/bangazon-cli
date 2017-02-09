import unittest
from customer import *
from order import *
from product import *

class TestAddProduct(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.bob = Customer("Albert", "Einstein","123 Atom Way",
                            "Apt. B2", "Nashville", "TN",
                            "32233", "615-555-555", "bigal@al.com")
        self.new_product = Product('yoyo', 5)
        self.active_order = Order(self.bob)

    def tearDown(self):
        self.active_order.total = 0

    def test_OrderIsActive(self):
        self.assertTrue(self.active_order.active)

    def test_OrderBelongsToActiveCustomer(self):
        self.assertIs(self.bob, self.active_order.get_customer())

    def test_OrderIncludesProductAdded(self):
        self.active_order.add_product(self.new_product)
        self.assertIn(self.new_product, self.active_order.products)

    def test_PriceOfProductAddedIsAddedToOrderTotal(self):
        self.active_order.add_product(self.new_product)
        self.assertEqual(self.new_product.price, self.active_order.get_total())
                            

if __name__ == '__main__':
    unittest.main()