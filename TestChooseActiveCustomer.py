import unittest
from customer import Customer
from superuser import Superuser

class TestChooseActiveCustomer(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.albert = Customer("Albert", "Einstein","123 Atom Way",
							"Apt. B2", "Nashville", "TN",
							"32233", "615-555-555", "bigal@al.com")
		self.superuser = Superuser()


	def test_superuser_can_choose_active_customer(self):
		
		self.superuser.activate_customer(self.albert)

		self.assertTrue(self.superuser.user_is_active(self.albert))

if __name__ == '__main__':
	unittest.main()
