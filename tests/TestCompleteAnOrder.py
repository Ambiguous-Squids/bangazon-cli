'''
This module defines the class to test Completing an Order
'''
import sys
sys.path.append('../')

import unittest
from customer import Customer
from payment_option import PaymentOption
from product import Product
from order import Order

class TestCompleteAnOrder(unittest.TestCase):
    '''
    Purpose:
        This class tests that a user can add a product to an order on behalf of the active customer.

    Methods:
        setUpClass(self)
        test_there_is_a_customer(self)
        test_customer_is_active(self)
        test_a_payment_option_has_been_created(self)
        test_a_product_is_in_order(self)
        test_no_products_in_order(self)
        test_payment_option_has_been_added_to_order(self)
        test_change_customer_from_active_to_inactive(self)

    Author: @nchemsak
    '''

    @classmethod
    def setUpClass(cls):
        cls.nick = Customer(
            "Nick",
            "Chemsak",
            "111 Street Rd",
            "suite 3",
            "Nashville",
            "TN",
            "37075",
            "123-123-0987",
            "test@test.com"
            )
        cls.order = Order("Nick", "Basketball", True, 1)
        cls.product = Product("Basketball", 5.00)
        cls.payment_option = PaymentOption(
            "Nick",
            "Chemsak",
            "1234567891234567",
            "2017-05-05",
            "123",
            "VISA"
            )
        cls.order2 = Order("Nick", "", True, 1)


    def test_there_is_a_customer(self):
        '''test that a customer exists'''
        self.assertIsInstance(self.nick, Customer)
        '''test that a customer can be registered to db'''
        self.nick.register_customer_in_db(self.nick)
        '''test that a customer is registered'''
        self.assertTrue(self.nick.customer_is_registered(self.nick))


    def test_customer_is_active(self):
        '''test that a customer is active'''
        self.nick.activate_customer()
        self.assertTrue(self.nick.user_is_active())


    def test_payment_option_created(self):
        '''test that a payment option has been created'''
        self.assertIsInstance(self.payment_option, PaymentOption)
        '''test that a payment option can be saved to db'''
        self.payment_option.save_to_db()
        '''test that a payment option exists in db'''
        self.assertTrue(self.payment_option.check_if_acct_exists())


    def test_a_product_is_in_order(self):
        '''test that a product is in the order'''
        self.order.add_product(self.product)
        self.assertIn(self.product, self.order.get_products(self.product))


    def test_no_products_in_order(self):
        '''test to see if there are no products in an order'''
        self.assertNotIn(self.product, self.order2.get_products(self.product))


    def test_payment_opt_add_to_order(self):
        '''test that a payment option has been added'''
        self.assertTrue(self.order.add_payment_option())


    def test_active_to_inactive(self):
        '''test that a customer can be changed from active to inactive'''
        self.assertFalse(self.nick.deactivate_customer())


if __name__ == '__main__':
    unittest.main()
