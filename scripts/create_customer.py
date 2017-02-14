import os
import sys
import main
sys.path.append('../')
from customer import Customer
from superuser import Superuser


def createCustomer(active_customer):

	'''
		Customer creation interface
		provides inputs to enter customer information
		passes inputs to superuser method 
		to register customer in db
		calls mainMenu() to return to main interface

		@rtwhitfield84
	'''

	os.system("clear")

	print("\n""******************************* \n"
		"** Create a Customer Account ** \n"
		"******************************* \n")


	print("\nEnter customer first name")
	first_name = str(input(">"))

	print("\nEnter customer last name")
	last_name = str(input(">"))

	print("\nEnter address 1")
	address_1 = str(input(">"))

	print("\nEnter address 2 (optional)")
	address_2 = str(input(">"))

	print("\nEnter city")
	city = str(input(">"))

	print("\nEnter state")
	state = str(input(">"))

	print("\nEnter zip code")
	zip_code = str(input(">"))

	print("\nEnter phone number")
	phone_number = str(input(">"))

	print("\nEnter email")
	email = str(input(">"))
	new_customer = Customer(first_name, last_name, address_1,
							address_2, city, state, zip_code,
							phone_number, email)
	Superuser.register_customer(object,new_customer)
	main.mainMenu(active_customer)




