import os
from create_customer import *

def mainMenu():

	'''
		Main command line user interface functionality

		Vars:
			choice - integer input for user choice
	'''

	os.system("clear")

	print("\n""******************************************************* \n"
		"** Welcome to Bangazon! Command Line Ordering System ** \n"
		"******************************************************* \n")
	print("1. Create a customer account \n")
	print("2. Choose active customer \n")
	print("3. Create a payment option \n")
	print("4. Add product to shopping cart \n")
	print("5. Complete an order \n")
	print("6. See product popularity \n")
	print("7. Leave Bangazon! \n")


	while True:
		'''enables continuous interface until user exits'''
		try:
			'''controls error'''
			choice = int(input())

			if choice == 1:
				createCustomer()
				break

			if choice == 2:
				chooseCustomer()
				break

			if choice == 3:
				createPayment()
				break

			if choice == 4:
				addProduct()
				break

			if choice == 5:
				completeOrder()
				break

			if choice == 6:
				getProductPopularity()
				break

			elif choice == 7:
				exit()
				break

			else:
				print("Please enter a valid choice")
		except ValueError:
				print("Please enter a valid choice")
	exit



if __name__ == '__main__':
	mainMenu()
