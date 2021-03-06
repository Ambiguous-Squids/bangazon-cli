import sys
sys.path.append('../')

import unittest
from customer import Customer
from superuser import Superuser

class TestCreateCustomer(unittest.TestCase):

	'''
	    Purpose:
	        This class tests that a customer can be created

	    Methods:
	        @classmethod
	        def setUpClass(self)
	        def test_superuser_can_create_customer_account(self):

	    Author:
	        @rtwhitfield84
	'''

	@classmethod
	def setUpClass(self):
		self.albert = Customer("Albert", "Einstein","123 Atom Way",
							"Apt. B2", "Nashville", "TN",
							"32233", "615-555-555", "bigal@al.com")
		self.superuser = Superuser()



	def test_superuser_can_create_customer_account(self):

		self.assertIsInstance(self.albert, Customer)
		self.superuser.register_customer(self.albert)
		self.assertTrue(self.albert.customer_is_registered(self.albert))


if __name__ == '__main__':
	unittest.main()
