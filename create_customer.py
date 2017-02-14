import os
from main import mainMenu
from customer import Customer
from superuser import Superuser

def createCustomer():

	os.system("clear")

	print("\n""******************************* \n"
		"** Create a Customer Account ** \n"
		"******************************* \n")

	while True:
		try:
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
			Superuser.register_customer(new_customer)
			mainMenu()

		except ValueError:
			print("Please enter a valid input")
	exit

if __name__ == '__main__':
	createCustomer()
