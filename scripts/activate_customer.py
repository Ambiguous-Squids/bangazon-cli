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

	customers = Superuser.get_customers()


	print("\n""*************************** \n"
		"** Login to your account ** \n"
		"*************************** \n")

	first_name = input("First name: ")
	last_name = input("Last name: ")

	password = ''

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

	for x in customers:
		print(x[0],":",x[1],x[2])

	choice = int(input("> "))
	print(choice)

	print('\n')
	input("-> Press any key to return to main menu")

	active_customer.set_active_customer()
	active_customer.set_active_customerId(choice)
	main.mainMenu(active_customer)
