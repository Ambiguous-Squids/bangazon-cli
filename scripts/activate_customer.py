import os
import sys
import main
sys.path.append('../')
from customer import Customer
from superuser import Superuser
from session_manager import SessionManager



def chooseCustomer(active_customer):

	'''
		Choose Customer interface
		provides list of users from db
		allows superuser to set active customer

		@rtwhitfield84
	'''

	os.system("clear")

	customers = Superuser.get_customers()

	print("\n""***************************** \n"
		"** Choose Active Customer ** \n"
		"***************************** \n")

	for x in customers:
		print(x[0],":",x[1],x[2])

	choice = int(input("> "))
	print(choice)

	active_customer.set_active_customer()
	active_customer.set_active_customerId(choice)
	main.mainMenu(active_customer)



