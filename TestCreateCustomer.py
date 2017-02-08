import unittest
<<<<<<< HEAD
from .customer import Customer
from .superuser import Superuser
=======
from customer import Customer
from superuser import Superuser
>>>>>>> 81c8c774b4902b61c32570acfc81ce7e674c6237


class TestCreateCustomer(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.albert = Customer("Albert", "Einstein","123 Atom Way",
							"Apt. B2", "Nashville", "TN",
							"32233", "615-555-555", "bigal@al.com")
		self.superuser = Superuser()



	def test_superuser_can_create_customer_account(self):

		self.assertIsInstance(self.albert, Customer)

		self.superuser.register_user(self.albert)
		self.assertTrue(self.superuser.user_is_registered(self.albert))




if __name__ == '__main__':
	unittest.main()



