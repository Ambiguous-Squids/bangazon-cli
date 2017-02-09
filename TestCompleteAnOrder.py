import unittest
from customer import Customer
from payment_option import PaymentOption
from product import Product
from order import Order

class TestCompleteAnOrder(unittest.TestCase):
    '''
    Author: @nchemsak
    '''

    @classmethod
    def setUpClass(self):
        print('set up class')
        self.customer = Customer("Nick", "Chemsak", "111 Street Rd", "suite 3", "Nashville", "TN", "37075", "123-123-0987", "test@test.com")
        self.order = Order("Nick", "Basketball", True, 1)
        self.product = Product("Basketball", 5.00)
        self.payment_option = PaymentOption("Nick", "Chemsak", "1234567891234567", "2017-05-05", "123", "VISA")
        self.order2 = Order("Nick", "", True, 1)


    def test_there_is_a_customer(self):
        self.assertIsInstance(self.customer, Customer)

    def test_customer_is_active(self):
        self.customer.activate_customer(self.customer)
        self.assertTrue(self.customer.user_is_active(self.customer))

    def test_a_payment_option_has_been_created(self):
        self.assertIsInstance(self.payment_option, PaymentOption)

    def test_a_product_is_in_order(self):
        self.order.add_product(self.product)
        self.assertIn(self.product, self.order.get_products(self.product))

    def test_no_products_in_order(self):
        self.assertNotIn(self.product, self.order2.get_products(self.product))

    def test_payment_option_has_been_added_to_order(self):
        self.assertTrue(self.order.add_payment_option())

    def test_change_customer_from_active_to_inactive(self):
        self.assertFalse(self.customer.deactivate_customer(self.customer))

if __name__ == '__main__':
    unittest.main()


