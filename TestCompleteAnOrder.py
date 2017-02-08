import unittest
from customer import Customer
from superuser import Superuser
from payment_option import PaymentOption

class TestCompleteAnOrder(unittest.TestCase):
    '''
    Author: @nchemsak
    '''

    @classmethod
    def setUpClass(self):
        print('set up class')
        self.nick = Customer("Nick", "Chemsak", "111 Street Rd", "suite 3", "Nashville", "TN", "37075", "123-123-0987", "test@test.com")
        self.superuser = Superuser()
        # self.order = Order("True")
        # self.product = Product("Basketball", "5.00", "1")
        self.credit = PaymentOption("Nick", "Chemsak", "1234567891234567", "2017-05-05", "123", "VISA")


    def test_user_is_active(self):
        self.superuser.activate_customer(self.nick)
        self.assertTrue(self.superuser.user_is_active(self.nick))

    def test_a_payment_option_has_been_created(self):
        self.assertIsInstance(self.credit, PaymentOption)

    def test_a_product_is_in_order(self):
        pass
        # self.superuser.add_product_to_order(self.order, self.product)
        # self.assertTrue(self.product_in_order)

    def test_no_products_in_order(self):
        pass

    def test_superuser_can_choose_payment_option(self):
        pass

    def test_change_customer_from_active_to_inactive(self):
        pass

if __name__ == '__main__':
    unittest.main()


