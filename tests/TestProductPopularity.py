"""
	This module defines the unittests for the user to see product popularity.

	Product 		Orders 			Customers 			Revenue
	============================================================
	Batteries		100				20					$999.90
	Cola			50				10					$5000.00
	Hat				25				5					$1000.50


"""


import unittest
from product import Product

class TestProductPopularity(unittest.TestCase):
	"""
		Purpose:
			This class tests that a table of products, orders, customers, and revenue will
			be returned.

		Methods:
			

		Author:
			@asimonia
	"""
	@classmethod
	def setUpClass(cls):
		cls.product = Product("basketball", 40)


	def test_product_popularity_returns_list_of_tuples(self):
		order_history = self.product.get_product_popularity_in_db()
		self.assertIsInstance(order_history, list)
		for order in order_history:
			self.assertIsInstance(order, tuple)




if __name__ == '__main__':
	unittest.main()