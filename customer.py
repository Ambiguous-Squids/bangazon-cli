import sqlite3
from password import Password

class Customer:

	'''
		Purpose:
			This class handles the creation of a Customer

		Methods:
			__init__(self, first_name, last_name, password, address_1,
							address_2, city, state, zip, phone_number, email)
			customer_is_active(self,customer)
			activate_customer(self,customer)
			deactivate_customer(self,customer)

		Author:
			@rtwhitfield84

	'''

	def __init__(self, first_name, last_name, password, address_1,
				address_2, city, state, zip, phone_number, email, is_active=False):

		self.__first_name = first_name
		self.__last_name = last_name
		self.__password = Password(password)
		self.__address_1 = address_1
		self.__address_2 = address_2
		self.__city = city
		self.__state = state
		self.__zip = zip
		self.__phone_number = phone_number
		self.__email = email
		self.__is_active = is_active

	@property
	def full_name(self):
		return "{} {}".format(self.__first_name, self.__last_name)

	@property
	def first_name(self):
		return self.__first_name

	@property
	def last_name(self):
		return self.__last_name

	@property
	def address_1(self):
		return self.__address_1

	@property
	def address_2(self):
		return self.__address_2
	@property
	def city(self):
		return self.__city

	@property
	def state(self):
		return self.__state

	@property
	def zip(self):
		return self.__zip

	@property
	def phone_number(self):
		return self.__phone_number

	@property
	def email(self):
		return self.__email

	@property
	def password(self):
		return self.__password.get_hashed_password()

	@property
	def is_active(self):
		return self.__is_active

	@property
	def customer_is_active(self, customer):
		return True

	def activate_customer(self):
		self.is_active = True

	def deactivate_customer(self):
		self.is_active = False


	def register_customer_in_db(self, customer):

		with sqlite3.connect("../bangazon.db") as b:
					cursor = b.cursor()

					cursor.execute("""
					INSERT OR IGNORE INTO Customers VALUES (null, '{}', '{}', '{}', '{}', '{}',
												'{}', '{}', '{}', '{}', '{}')
					""".format(
								customer.first_name,
								customer.last_name,
								customer.password,
								customer.address_1,
								customer.address_2,
								customer.city,
								customer.state,
								customer.zip,
								customer.phone_number,
								customer.email
								)
					)


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
