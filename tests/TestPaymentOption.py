'''
This module defines the class to test Payment Option creation.
'''
import sys
sys.path.append('../')

import unittest
from payment_option import PaymentOption


class TestCreatePaymentOption(unittest.TestCase):
    '''
    Purpose:
        This Class Tests that one can successfully create a Payment Option.

    Methods:
        setUpClass(cls)
        test_can_create_payment_option_in_db(self)
        test_created_payment_option_has_valid_first_name(self)
        test_created_payment_option_has_valid_last_name(self)
        test_created_payment_option_has_acct_number(self)
        test_created_payment_option_has_valid_exp_date(self)
        test_created_payment_option_has_valid_ccv(self)
        test_created_payment_option_has_valid_category(self)

    Author:
        @mccordgh
    '''

    @classmethod
    def setUpClass(cls):
        # This method creates a global instance of PaymentType to use in the following tests
        cls.payment_option = PaymentOption(
            "Matthew",
            "McCord",
            1234432156788765,
            "10/10/2019",
            432,
            "MASTERCARD"
            )

    def test_can_create_payment_option(self):
        '''test that payment option created in setUpClass is an instance of PaymentOption'''
        self.assertIsInstance(self.payment_option, PaymentOption)

    def test_created_first_name(self):
        '''test that payment option created in setUpClass has a valid first name'''
        self.assertEqual(self.payment_option.first_name, 'Matthew')

    def test_created_last_name(self):
        '''test that payment option created in setUpClass has a valid last name'''
        self.assertEqual(self.payment_option.last_name, 'McCord')

    def test_created_acct_number(self):
        '''test that payment option created in setUpClass has a valid account number'''
        self.assertEqual(self.payment_option.acct_number, 1234432156788765)

    def test_created_exp_date(self):
        '''test that payment option created in setUpClass has a valid expiration date'''
        self.assertEqual(self.payment_option.exp_date, '10/10/2019')

    def test_created_ccv(self):
        '''test that payment option created in setUpClass has a valid CCV security number'''
        self.assertEqual(self.payment_option.ccv, 432)

    def test_created_category(self):
        '''test that payment option created in setUpClass has a valid category name'''
        self.assertEqual(self.payment_option.category, 'MASTERCARD')

if __name__ == '__main__':
    unittest.main()
