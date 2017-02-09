import sqlite3

class Customer():

	'''
		Purpose:
			This class handles the creation of a Customer

		Methods:
			__init__(self, first_name, last_name, address_1,
							address_2, city, state, zip, phone_number, email)
			user_is_active(self,user)
			activate_customer(self,user)
			deactivate_customer(self,user)

		Author:
			@rtwhitfield84

	'''

	def __init__(self, first_name, last_name, address_1,
				address_2, city, state, zip, phone_number, email):

		self.first_name = first_name
		self.last_name = last_name
		self.address_1 = address_1
		self.address_2 = address_2
		self.city = city
		self.state = state
		self.zip = zip
		self.phone_number = phone_number
		self.email = email


	def user_is_active(self,user):
		return True

	def activate_customer(self,user):
		pass

	def deactivate_customer(self,user):
		return False
