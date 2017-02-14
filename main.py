import os
import create_customer
def mainMenu():

	'''
		Main command line user interface functionality

		Vars:
			choice - integer input for user choice

		@rtwhitfield84
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



	'''controls error'''
	try:
		choice = int(input())

		if choice == 1:
			create_customer.createCustomer()
			

		if choice == 2:
			pass
			# chooseCustomer()
			

		if choice == 3:
			pass
			# createPayment()
			

		if choice == 4:
			pass
			# addProduct()
			

		if choice == 5:
			pass
			# completeOrder()
			

		if choice == 6:
			pass
			# getProductPopularity()
			

		elif choice == 7:
			exit()
			

		else:
			print("Please enter a valid choice")
	except ValueError:
			print("Please enter a valid choice")




if __name__ == '__main__':
	mainMenu()
