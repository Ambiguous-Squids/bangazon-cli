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

	def get_full_name(self):
	    return "{} {}".format(self.first_name, self.last_name)

	def get_first_name(self):
	    return str(self.first_name)

	def get_last_name(self):
	    return str(self.last_name)

	def get_address_1(self):
	    return str(self.address_1)

	def get_address_2(self):
	    return str(self.address_2)

	def get_city(self):
		return str(self.city)

	def get_state(self):
		return str(self.state)

	def get_zip(self):
		return str(self.state)

	def get_phone_number(self):
		return str(self.phone_number)

	def get_email(self):
	    return str(self.email)

	def user_is_active(self,user):
		return True

	def activate_customer(self,user):
		pass

	def deactivate_customer(self,user):
		return False


	def register_user_in_db(self,user):

		with sqlite3.connect("bangazon.db") as b:
		            cursor = b.cursor()

		            cursor.execute("""
		            INSERT INTO Customer VALUES (null, '{}', '{}', '{}', '{}')
		            """.format(
		                        get_first_name(), 
		                        get_last_name(), 
		                        get_address_1(), 
		                        get_address_2(), 
		                        get_city(), 
		                        get_state(), 
		                        get_zip(), 
		                        get_phone_number(), 
		                        get_email()))



