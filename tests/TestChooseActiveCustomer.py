import sys
sys.path.append('../')

import unittest
from customer import Customer
from session_manager import SessionManager

class TestChooseActiveCustomer(unittest.TestCase):

	'''
	    Purpose:
	        This class tests that a user can be chosen as active

	    Methods:
	        @classmethod
	        def setUpClass(self)
	        def test_superuser_can_choose_active_customer(self):

	    Author:
	        @rtwhitfield84
	'''

	@classmethod
	def setUpClass(self):
		self.albert = Customer("Albert", "Einstein","123 Atom Way",
							"Apt. B2", "Nashville", "TN",
							"32233", "615-555-555", "bigal@al.com")
		self.session_manager = SessionManager()


	def test_superuser_can_choose_active_customer(self):
		
		self.session_manager.set_active_customer()

		self.assertTrue(self.session_manager.get_active_customer())

if __name__ == '__main__':
	unittest.main()
