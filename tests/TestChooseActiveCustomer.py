import sys
sys.path.append('../')

import unittest
from customer import Customer
from session_manager import SessionManager

class TestChooseActiveCustomer(unittest.TestCase):

	'''
	    Purpose:
	        This class tests that a customer can be set as active

	    Methods:
	        def test_superuser_can_choose_active_customer(self):

	    Author:
	        @rtwhitfield84
	'''




	def test_session_manager_can_set_active_customer(self):

		self.session_manager = SessionManager()
		
		self.session_manager.set_active_customer()

		self.assertTrue(self.session_manager.get_active_customer())

if __name__ == '__main__':
	unittest.main()
