import sys
sys.path.append('../')

import unittest
from customer import *
from order import *
from product import *
from payment_option import *


class TestAddProduct(unittest.TestCase):

    """
    Purpose:
        This class tests that a user can add a product to an order on behalf of the active customer.

    Methods:
        setUp(self)
        tearDown(self)
        test_OrderIsActive(self)
        test_OrderBelongsToActiveCustomer(self)
        test_OrderIncludesProductAdded(self)
        test_PriceOfProductAddedIsAddedToOrderTotal(self)

    Author:
        @alirk
    """

    @classmethod
    def setUpClass(cls):
        cls.bob = Customer(
            "Albert",
            "Einstein",
            "123 Atom Way",
            "Apt. B2",
            "Nashville",
            "TN",
            "32233",
            "615-555-555",
            "bigal@al.com"
            )
        cls.spiderman = Product('Spiderman', 5)
        cls.basketball = Product('Basketball', 6)
        cls.baseball = Product('Baseball', 7)
        cls.payment_option = PaymentOption(
            "Matthew",
            "McCord",
            1234432156788765,
            "10/10/2019",
            432,
            "MASTERCARD"
            )
        cls.active_order = Order(
            cls.bob,
            [cls.basketball, cls.baseball],
            True,
            cls.payment_option,
            2
            )


    @classmethod
    def tearDown(self):
        self.active_order.total = 0

    def test_order_is_active(self):
        self.assertTrue(self.active_order.is_active())

    def test_order_belongs_to_active_customer(self):
        self.assertIs(self.bob, self.active_order.get_customer())

    def test_order_product_saved_to_db(self):
        self.active_order.add_product(self.spiderman)
        self.assertIn("Legend of Zelda", self.active_order.get_products())

    def test_price_of_product_added_is_added_to_order_total(self):
        self.assertEqual(18, self.active_order.get_total())

    def test_payment_option_saved_to_db(self):
        self.payment_option.save_to_db()
        self.assertTrue(self.payment_option.check_if_acct_exists())

if __name__ == '__main__':
    unittest.main()
