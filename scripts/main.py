import os
import sys
import create_customer
import activate_customer
import create_payment_option
import show_productpopularity
import session_manager
import add_product


sys.path.append('../')



def mainMenu(active_customer):

	'''
		Main command line user interface functionality

		Vars:
			choice - integer input for user choice

		@rtwhitfield84
	'''

	os.system("clear")


	while True:
		print("\n""******************************************************* \n"
			"** Welcome to Bangazon! Command Line Ordering System ** \n"
			"******************************************************* \n")
		print("1. Create a customer account")

		if active_customer.active_customer:
			print("2. Logout of my account")
		else:
			print("2. Login into my account")
		print("3. Create a payment option")
		print("4. Add product to shopping cart")
		print("5. Complete an order")
		print("6. See product popularity")
		print("7. Leave Bangazon!")
		'''controls error'''
		try:
			choice = int(input("> "))

			if choice == 1:
				create_customer.createCustomer(active_customer)
				

			if choice == 2:
				if active_customer.active_customer:
					# A customer is active, so logout customer
					active_customer.deactivate_customer()
					print("Logging out...")
					print('\n')
					input("-> Press any key to return to main menu")
					os.system("clear")
					continue
				else:
					# A customer is inactive, so login customer
					activate_customer.chooseCustomer(active_customer)
				

			if choice == 3:
				create_payment_option.createPaymentOption(active_customer)
		
		
			if choice == 4:
				add_product.startOrder(active_customer)
		
			if choice == 5:
				if active_customer.get_active_orderId() == None:
					print("There is no active order")

			if choice == 6:
				show_productpopularity.show_product_popularity(active_customer)		

			elif choice == 7:
				break
				

			else:
				print("Please enter a valid choice")
				print('\n')
				input("-> Press any key to return to main menu")
				os.system("clear")
		except ValueError:
				print("Please enter a valid choice")
				print('\n')
				input("-> Press any key to return to main menu")
				os.system("clear")

	exit()

if __name__ == '__main__':
	active_customer = session_manager.SessionManager()
	mainMenu(active_customer)
