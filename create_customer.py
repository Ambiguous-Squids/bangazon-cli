import os

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
			adress_1 = str(input(">"))

			print("\nEnter address 2 (optional)")
			adress_2 = str(input(">"))

			print("\nEnter city")
			city = str(input(">"))

			print("\nEnter state")
			state = str(input(">"))

			print("\nEnter zip code")
			zip = str(input(">"))

			print("\nEnter phone number")
			adress_1 = str(input(">"))

			print("\nEnter email")
			email = str(input(">"))
			break

		except ValueError:
			print("Please enter a valid input")
	exit

if __name__ == '__main__':
	createCustomer()
