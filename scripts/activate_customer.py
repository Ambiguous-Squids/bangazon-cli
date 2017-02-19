import os
import sys
import main
sys.path.append('../')
from customer import Customer
from superuser import Superuser
from session_manager import SessionManager
from getpass import getpass




def chooseCustomer(active_customer):

	'''
		Choose Customer interface
		provides list of users from db
		allows superuser to set active customer

		@rtwhitfield84
		@asimonia
	'''

	os.system("clear")

	# Fetch the customer id, first name, last name, password
	# assign it to customers as a list of tuples
	selected = False
	customers = Superuser.get_customers()
	password = ''
	choice = 0


	print("\n""*************************** \n"
		"** Login to your account ** \n"
		"*************************** \n")

	# Select the first and last name for the customer
	# Test to see if it in customers
	
	while not selected:

		first_name = input("First name: ")
		last_name = input("Last name: ")

		for customer in customers:
			if customer[1] == first_name and customer[2] == last_name:
				# Once customer is selected, get password
				print("Welcome {} {}!\n".format(first_name, last_name))
				choice = customer[0]
				password = customer[3]
				selected = True

		if not selected:
			print("Please enter a valid customer.\n")

	print("choice " + str(choice))
	print("password " + str(password))
	# Mask characters for password input
	# Compare against re-entry

	while True:
		password_a = getpass()
		password_b = getpass(prompt="Re-enter password: ")

		if password_a == password_b:
			password = str(password_a)
			break
		else:
			print("Passwords must match!\n")

	print('\n')
	input("-> Press any key to return to main menu")

	active_customer.set_active_customer()
	active_customer.set_active_customerId(choice)
	main.mainMenu(active_customer)
