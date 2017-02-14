import sqlite3

class Customer():

	'''
		Purpose:
			This class handles the creation of a Customer

		Methods:
			__init__(self, first_name, last_name, address_1,
							address_2, city, state, zip, phone_number, email)
			customer_is_active(self,customer)
			activate_customer(self,customer)
			deactivate_customer(self,customer)

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
		return str(self.zip)

	def get_phone_number(self):
		return str(self.phone_number)

	def get_email(self):
	    return str(self.email)

	def customer_is_active(self,customer):
		return True

	def activate_customer(self,customer):
		pass

	def deactivate_customer(self,customer):
		return False


	def register_customer_in_db(self,customer):

		with sqlite3.connect("../bangazon.db") as b:
		            cursor = b.cursor()

		            cursor.execute("""
		            INSERT OR IGNORE INTO Customers VALUES (null, '{}', '{}', '{}', '{}',
		            							'{}', '{}', '{}', '{}', '{}')
		            """.format(
		                        customer.get_first_name(), 
		                        customer.get_last_name(), 
		                        customer.get_address_1(), 
		                        customer.get_address_2(), 
		                        customer.get_city(), 
		                        customer.get_state(), 
		                        customer.get_zip(), 
		                        customer.get_phone_number(), 
		                        customer.get_email()))


	def customer_is_registered(self,customer):
		with sqlite3.connect("../bangazon.db") as b:
		    cursor = b.cursor()

		    try:
		        cursor.execute("""
		            SELECT * FROM Customers 
		            WHERE email='{}'
		        """.format(customer.get_email()))
		    except sqlite3.OperationalError:
		        return False

		    customer = cursor.fetchall()
		    return len(customer) == 1
